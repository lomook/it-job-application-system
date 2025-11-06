# IT岗位求职记录系统

## 项目介绍

这是一个基于Flask框架开发的IT岗位求职记录系统，支持岗位信息的添加、编辑、删除和查询功能。

## 技术栈

- **后端**：Flask、SQLAlchemy、SQLite
- **前端**：HTML、Tailwind CSS、Font Awesome
- **表单处理**：Flask-WTF

## 项目结构

```
.
├── .gitignore          # Git忽略文件
├── app.py              # 主程序文件
├── jobs.db             # SQLite数据库文件
├── requirements.txt    # 项目依赖
├── README.md           # 项目说明文档
└── templates/          # HTML模板文件夹
    ├── add_job.html    # 添加岗位页面
    ├── edit_job.html   # 编辑岗位页面
    └── index.html      # 岗位列表页面
```

## Git操作指南

### 1. 初始化本地仓库

```bash
# 在项目根目录下执行
git init
git config --global user.name "您的GitHub用户名"
git config --global user.email "您的GitHub邮箱"
```

### 2. 添加和提交文件

```bash
# 添加所有文件
git add .

# 提交更改
git commit -m "Initial commit - IT岗位求职记录系统"
```

### 3. 关联远程仓库

```bash
# 关联GitHub仓库
git remote add origin https://github.com/您的用户名/it-job-application-system.git

# 重命名分支为main
git branch -M main
```

### 4. 推送到远程仓库

```bash
# 推送代码到GitHub
git push -u origin main
```

### 5. 从远程仓库拉取更新

```bash
# 拉取最新代码
git pull origin main
```

### 6. 克隆仓库

```bash
# 克隆仓库到本地新目录
git clone https://github.com/您的用户名/it-job-application-system.git 新目录名
```

## 运行项目

1. 安装依赖：
```bash
pip install -r requirements.txt
```

2. 运行应用：
```bash
python app.py
```

3. 访问系统：
   打开浏览器，访问 http://127.0.0.1:5000

## 功能说明

- **岗位列表**：查看所有求职岗位记录，支持按公司名称、岗位名称和状态筛选
- **添加岗位**：录入新的求职岗位信息
- **编辑岗位**：修改现有岗位信息
- **删除岗位**：删除不需要的岗位记录
- **状态更新**：可更新岗位申请状态（待投递、已投递、面试中、已录用、已拒绝）

## 开发者信息

- **姓名**：罗茂锟
- **学号**：20234272
