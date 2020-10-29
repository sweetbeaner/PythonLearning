#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  16:27
# !@Author : SweetBeaner
# !@File :.py
# !@Information :
# 练习： 接收用户输入的一个字符串数据，判断字符串里面是否有某一个字符，如果有则打印出来，否则显示没有指定数据

inp = input("请输入一个字符串")
s = "i"
for i in inp:
    if i ==s:
        print(i)
    else:
        print("没有指定数据")