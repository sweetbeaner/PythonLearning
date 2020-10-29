#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  14:16
# !@Author : Sweetbeaner
# !@File :.py
# !@Information :

# 函数的嵌套调用:在一个函数里面又调用了其它函数，该形式成为函数的嵌套调用


def task1():
    print("task1开始执行了")
    print("task1...")
    print("task1执行结束了")


def task2():
    print("task2开始执行了")
    # 调用task1函数
    task1()
    print("task2执行结束了")


task2()

# 练习: 已知上面的提供的代码，写出调用task2函数后的执行流程
print("task2开始执行了")
print("task1开始执行了")
print("task1...")
print("task1执行结束了")
print("task2执行结束了")