#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  15:35
# !@Author : Sweetbeaner
# !@File :.py
# !@Information :

# * #### 题目1

# 定义一个函数max，接受的参数类型是数值，最终返回两个数中的最大值

##### 训练提示

# 第一步：定义一个函数max
#
# 第二步：定义两个形参
#
# 第三步：通过比较这两个参数返回其中较大的
# def max(a,b):
#     if a>b:
#         return a
#     elif a<b:
#         return b
#     else:
#         return '相等'
# print(max(3,4))

### 题目2

# 定义一个函数 sum_random 接收二个参数 m, n ，在函数中计算 m + n 的值，并打印结果，要求 m 和 n 是 1 -- 100 之间的数

##### 训练提示

# def sum_random(m, n):
#     if (m>0 and m<=100) and (n>0 and n)<=100:
#         return m + n
# print(sum_random(99, 99))


### 题目3

# 用函数实现一个判断用户输入的年份是否是闰年的程序，在函数中打印结果。
# def yearJudge():
#     year = int(input('请输入一个年份：'))
#     if year%4==0:
#         print(year,'是闰年')
#     else:
#         print(year,'不是闰年')
# yearJudge()

### 题目4

# 定义一个函数，计算两个数之和。调用者在得到结果的时候需要判断是否大于20，如果大于则输出，超过10的加法太难了
# def sumJudege(a, b):
#     sum = a + b
#     if sum > 20:
#         print('超过10的加法太难了')
#     return sum
#
#
# sumJudege(3, 18)


# 拓展提高
### 题目1

# 定义一个函数cut_str，接受三个参数，分别为字符串s、数值a1、数值a2，将字符串s从下标a1开始的a2个字符删除，并把结果返回
#
# 例如：
#
# ```python
# s = "123456789", a1 = 2, a2 = 4
# 结果为: "12789"

# def cut_str(s, a1, a2):
#     s1 = s[:a1]
#     s2 = s[a1 + a2:]
#     return s1 + s2
#
#
# print(cut_str('1234567890', 3, 5))


### 题目2

# 请定义两个函数，一个函数打印正方形，一个函数打印三角形，并且可以从键盘输入值来决定打印矩形还是打印三角形以及决定是否退出程序

##### 训练提示

# 1、函数的定义
#
# 2、函数的调用
#
# 3、逻辑判断以及循环
#
# 思路提示 ：定义两个函数，一个函数打印三角形，一个函数打印矩形，通过判断用户输入来决定调用哪个函数

# def sjx():
#     print('三角形')
# def zfx():
#     print('正方形')
#
# if int(input('请输入一个数字:'))==1:
#     sjx()
# else:
#     zfx()

### 题目3

# 定义一个函数，这个函数需要接收的参数不确定多少个，请实现

# def funcTest(*args):
#     print(args)
#
#
# funcTest(1, 3, 4, "哈哈哈", "测试一下", ('什么鬼', '无聊'))

### 题目4

# 有变量 a = 10 和 b = 20 ，请使用至少两种方法交换两个变量的值。
# a = 10
# b = 20
#
#
# def change_1(a, b):
#     c = a
#     a = b
#     b = c
#     return a, b
#
#
# print(change_1(3, 4))
#
#
# def change_2(a, b):
#     return b, a
#
#
# print(change_2(3, 4))
