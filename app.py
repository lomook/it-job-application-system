from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, NumberRange
import os
from datetime import datetime

# 初始化Flask应用
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

# 配置数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 初始化数据库
db = SQLAlchemy(app)

# 定义岗位数据模型
class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(100), nullable=False)
    job_title = db.Column(db.String(100), nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    requirements = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text)
    location = db.Column(db.String(100))
    status = db.Column(db.String(20), default='未申请')  # 未申请、已申请、面试中、已录用、已拒绝

# 创建数据库表
with app.app_context():
    db.create_all()

# 定义添加岗位表单
class JobForm(FlaskForm):
    company_name = StringField('企业名称', validators=[DataRequired()])
    job_title = StringField('岗位名称', validators=[DataRequired()])
    salary = IntegerField('薪资(元/月)', validators=[DataRequired(), NumberRange(min=0)])
    requirements = TextAreaField('具体要求', validators=[DataRequired()])
    description = TextAreaField('岗位职责')
    location = StringField('工作地点')
    status = StringField('申请状态')
    submit = SubmitField('提交')

# 主页路由 - 显示岗位列表
@app.route('/', methods=['GET', 'POST'])
def index():
    # 获取筛选参数
    search = request.args.get('search', '')
    status_filter = request.args.get('status', '')
    
    # 构建查询
    query = Job.query
    
    # 应用搜索筛选
    if search:
        query = query.filter(
            (Job.company_name.contains(search)) |
            (Job.job_title.contains(search)) |
            (Job.requirements.contains(search))
        )
    
    # 应用状态筛选
    if status_filter:
        query = query.filter_by(status=status_filter)
    
    # 获取所有岗位
    jobs = query.order_by(Job.id.desc()).all()
    
    # 获取所有状态用于筛选下拉框
    statuses = db.session.query(Job.status).distinct().all()
    status_list = [status[0] for status in statuses]
    
    return render_template('index.html', jobs=jobs, search=search, status_filter=status_filter, status_list=status_list)

# 添加岗位路由
@app.route('/add', methods=['GET', 'POST'])
def add_job():
    form = JobForm()
    if form.validate_on_submit():
        # 创建新岗位
        new_job = Job(
            company_name=form.company_name.data,
            job_title=form.job_title.data,
            salary=form.salary.data,
            requirements=form.requirements.data,
            description=form.description.data or '',
            location=form.location.data or '',
            status=form.status.data or '未申请'
        )
        
        # 保存到数据库
        db.session.add(new_job)
        db.session.commit()
        
        flash('岗位添加成功！')
        return redirect(url_for('index'))
    
    return render_template('add_job.html', form=form)

# 编辑岗位路由
@app.route('/edit/<int:job_id>', methods=['GET', 'POST'])
def edit_job(job_id):
    job = Job.query.get_or_404(job_id)
    form = JobForm(obj=job)
    
    if form.validate_on_submit():
        # 更新岗位信息
        job.company_name = form.company_name.data
        job.job_title = form.job_title.data
        job.salary = form.salary.data
        job.requirements = form.requirements.data
        job.description = form.description.data or ''
        job.location = form.location.data or ''
        job.status = form.status.data or '未申请'
        
        # 保存到数据库
        db.session.commit()
        
        flash('岗位信息更新成功！')
        return redirect(url_for('index'))
    
    return render_template('edit_job.html', form=form, job=job)

# 删除岗位路由
@app.route('/delete/<int:job_id>', methods=['POST'])
def delete_job(job_id):
    job = Job.query.get_or_404(job_id)
    db.session.delete(job)
    db.session.commit()
    flash('岗位已成功删除！')
    return redirect(url_for('index'))

# 添加模板上下文处理器，使now函数在所有模板中可用
@app.context_processor
def inject_now():
    return {'now': datetime.now}

if __name__ == '__main__':
    app.run(debug=True)