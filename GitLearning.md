# Git简明学习
## 1.Git的安装与配置
### 1.1Git的安装

https://git-scm.com/download/win

### 1.2Git的使用入口

进入git bash或者终端

### 1.3Git的基础配置

* 首次使用说明身份：配置User和Email，并非注册，仅仅作为身份标识使用

git config --global user.name "姓名"
git config --global user.email 邮箱

* 创建仓库

在项目文件夹下的git bash中初始化：git init 

使用他人的git创建仓库：git clone 项目url

## 2.状态与提交版本

### 2.1 跟踪Track

* 跟踪文件

git add <file_name>

* 各种当前目录

git add .

### 2.2 取消跟踪Untrack

* rm 删除

git rm <file_name>

* 保留但不跟踪

git rm-cache <file_name>

### 2.3 文件的修改

* 将修改后的文件暂存

git add <file_name>

* 取消暂存

git reset HEAD <file_name>

* 提交暂存的修改

git commit <file_name>：进入提交页面类似vim，按i进行输入文本，按Esc结束编辑，按:进入命令栏，输入wq保存并退出

git commit <file_name> -m '提交说明'

* 连带未暂存文件一起提交

git commit -am '提交说明'

*  撤回本次提交

git reset head~ --soft：无法撤回首次提交

### 2.4 查看状态

#### 2.4.1 git status

* 红色：已修改且未暂存
* 绿色：已暂存
* 不现实：已经完成提交
* Untracked Files：未进行add跟踪（track）的代码

#### 2.4.2 git log

git log 查看历史提交信息

#### 2.4.3 git log --all

查看所有分值的历史提交

结合graph更好

git log --all --graph

![image](https://github.com/sweetbeaner/PythonLearning/assets/45441850/e44e9d5c-6589-45a9-b080-a81e8d21d5fb)

## 3.远程仓库

可以使用github等进行托管

* 连接远程仓库：git remote add 仓库/项目名 远程仓库连接

* 修改远程仓库名称：git remote rename 目标仓库名 修改后的名称 

* 推送到远程仓库： git push 仓库名 分支名

可以使用token令牌或者ssh鉴权进行授权，具体参考github文档

## 4.分支Branch

分支的意义：规范化开发、测试和发布过程

![image](https://github.com/sweetbeaner/PythonLearning/assets/45441850/e2174dfe-a849-4773-983e-8d12aa3e7550)

### 4.1 查看当前分支

* git status
* git branch --list
* git log

### 4.2 创建分支

git branch 分支名

git checkout -b 分支名

### 4.3 切换分支

git checkout 分支名

