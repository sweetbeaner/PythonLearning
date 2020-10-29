#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  15:54
# !@Author : SweetBeaner
# !@File :.py
# !@Information :复杂条件语句
# if-else语句语法格式


# ==============根据以下注释，完成相关的代码练习==========

# 接收用户输入的用户名和密码，当用户名及密码都输入正确输出登录成功，
# 否则输出用户名或者密码错误
username = "SweetBeaner"
pwd = "SweetBeaner"
inputName = input("请输入用户名：")
inputPwd = input("请输入密码：")
if username == inputName and pwd == inputPwd:
    print("登录成功")
else:
    print("登录失败")
