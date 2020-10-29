#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  15:26
# !@Author : Sweetbeaner
# !@File :.py
# !@Information :

# 练习: 文件夹及文件夹的相关操作

# 1. 对1.txt 文件进行重命名
import os
# os.rename('test.txt','newTest.txt')
# 2. 删除2.txt 文件
# os.remove('newTest.txt')
# 3. 创建文件夹AAA
# os.mkdir('AAA')
# 4. 查看当前操作文件夹路径
# print(os.getcwd())
# 5. 切换到指定文件夹AAA
# os.chdir('AAA')
print(os.getcwd())
# 6. 查看指定目录AAA里面的所有文件名
os.listdir('./')
# 7. 删除空文件夹
os.rmdir('AAA')
# 8. 删除非空文件夹
# 9. 判断1.txt文件是否存在