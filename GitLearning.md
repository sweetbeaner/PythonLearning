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

git commit <file_name>，进入提交页面类似vim，按i进行输入文本，按Esc结束编辑，按:进入命令栏，输入wq保存并退出

git commit <file_name> -m '修改说明'
*  
* 


  
  
  
  
  ![image](https://github.com/sweetbeaner/PythonLearning/assets/45441850/e44e9d5c-6589-45a9-b080-a81e8d21d5fb)
