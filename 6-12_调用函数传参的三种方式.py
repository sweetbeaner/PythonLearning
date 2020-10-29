#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  14:51
# !@Author : Sweetbeaner
# !@File :.py
# !@Information :


def show(name, age=18):
    print("姓名:", name, "年龄:", age)

# 练习：已知上面的函数，在调用函数时使用三种方式进行传参

show('Sweetbeaner')
show('Sweetbeaner',20)
show(name='Sweetbeaner',age=20)