#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  17:02
# !@Author : SweetBeaner
# !@File :.py
# !@Information :

# 练习：接收用户输入的两个数据姓名、性别，使用fstring的方式进行输出

name = input('请输入用户姓名')
sex = input('请输入性别')
fmat_str = f'用户姓名为：{name}，性别为：{sex}'
print(fmat_str)