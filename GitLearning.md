![image](https://github.com/sweetbeaner/PythonLearning/assets/45441850/41862366-3096-44c0-acdd-cc65815b021c)# Git简明学习
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

查看所有分支的历史提交

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

### 4.4 合并分支

#### 4.4.1 合并两个分支

git merge 分支名

如果两个分支修改相同位置内容的话会报错

![image](https://github.com/sweetbeaner/PythonLearning/assets/45441850/83677947-49f0-4ec1-a9b7-e033f6d1e67d)

通过git status查看冲突位置

![image](https://github.com/sweetbeaner/PythonLearning/assets/45441850/8b8015c6-89c6-4f6e-8f61-c35e9da8e88f)

进入相关文件，"======="上为当前分支上的修改，下为想要合并的分支的修改

![image](https://github.com/sweetbeaner/PythonLearning/assets/45441850/98cd5d04-cf40-4717-9cfa-ea5cddc23508)

处理完冲突后，保存当前文件并进行git add <文件名>

随后进行commit，并可通过git log --all --graph 看到合并路径

![image](https://github.com/sweetbeaner/PythonLearning/assets/45441850/24e87b43-d15f-4925-8a4a-513b30a53237)

#### 4.4.2 远程拉取分支

git checkout 远程分支

git checkout -b 远程跟踪分支

git checkout --track 远程分支

## 5.git的储藏功能

如果写到一半时，需要处理其他分支，不建议把当前分支进行提交，而是先用stash储存起来

git stash

git stash push

![image](https://github.com/sweetbeaner/PythonLearning/assets/45441850/32e74ec0-103e-4fa4-9036-62ecb1aadb64)

如果当前branch存在已修改但未提交的内容，则会出现如下提示

![image](https://github.com/sweetbeaner/PythonLearning/assets/45441850/58a2afc8-1d37-401d-acc5-bd603d30fd11)

通过 git stash进行储存，储存完成后当前状态没有未提交内容

![image](https://github.com/sweetbeaner/PythonLearning/assets/45441850/aa107910-6a55-4ba4-8eed-55f27a1902fb)

处理完其他分支事宜后，反回stash内容的分支，通过git stash apply恢复原本正在编辑的内容

![image](https://github.com/sweetbeaner/PythonLearning/assets/45441850/87556bfc-1e4c-4364-8e6d-fd19e9297baa)


如果存在多次存储stash，则能够通过git stash list进行存储内容的查看

![image](https://github.com/sweetbeaner/PythonLearning/assets/45441850/ea4060b7-e29b-4c0b-bb27-3d1d89070760)

如果想恢复某一次的存储，可以通过git stash apply stash@{n}，其中n为list中的内容

![image](https://github.com/sweetbeaner/PythonLearning/assets/45441850/55a6b972-0f14-4865-8475-a87083f187fa)

如果想恢复最后一次的存储并且删除其他存储，可以使用git stash pop命令

![image](https://github.com/sweetbeaner/PythonLearning/assets/45441850/b2608b3b-3100-4ca5-97c3-2822948d8f72)

如果想删除最后一次的stash，可以使用git stash drop stash@{0}命令，只删除最新的stash，过去的往前顺延

![image](https://github.com/sweetbeaner/PythonLearning/assets/45441850/0dad9273-b297-405b-afc7-51d7576ed07a)

## 6.reset命令

### 6.1 head命令

* head：当前的提交

* head~：上一次的提交

* head~3:倒数第二次或者第3次的提交

* --soft：只撤回提交操作，暂存状态还存在

* --hard：彻底取消，反回上一次刚提交完的状态

### 6.2 rebase变基

搬家操作：可以让提交记录变得好看

git rebase A，将B上的修改移至A分支

![image](https://github.com/sweetbeaner/PythonLearning/assets/45441850/88aa5e65-1731-44e2-b39d-53606ba67f42)

git rebase -i head~n,n为前几次修改，可以进行修改

![image](https://github.com/sweetbeaner/PythonLearning/assets/45441850/e9ffc410-1f1a-4804-a40a-eefb6dedaf86)

可以将多次提交融合成一次提交
