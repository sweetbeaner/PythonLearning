#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  15:12
# !@Author : Sweetbeaner
# !@File :.py
# !@Information :

# 练习1: 定义一个函数完成缺省参数结合不定长位置参数使用

def test1(a=0,b=5,*args):
    sum= a+b
    for i in args:
        sum = sum+i
    print(sum)

test1(1,2,3,45)

# 练习2: 定义一个函数完成缺省参数结合不定长位置参数和不定长关键字参数的使用

def test2(a=1,b=2,*args,**kwargs):
    print(args[0],kwargs)
    return a+b

test2(2,3,("你好","再见"),name='Sweetbeaner',age=20)