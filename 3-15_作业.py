#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  11:18
# !@Author : SweetBeaner
# !@File :.py
# !@Information :

# 使用while循环计算1~100的累加和（包含1和100）
# i = 1
# sum = 0
# while i <= 100:
#     sum = sum + i
#     i += 1
# print(sum)

# 设计“过7游戏”的程序, 打印出1-100之间除了7和7的倍数之外的所有数字，
# 如果遇见7和7的倍数则打印“哈~”跳过本次循环。
# i = 1
# while i <= 100:
#     if i % 7 != 0:
#         print(i)
#         i += 1
#     else:
#         print('哈')
#         i += 1
#         continue
# 从键盘上输入一个字母，判断此字母是否在变量 a 中，
# 如果在则输出 找到了， 如果不在 则输出 查无此字母
# a = "itheima"
# inp = input('请输入一个字母')
# for i in a:
#     if i == inp:
#         print('找到了')
#         break
# else:
#     print('查无此字母')

# 要求用户输入一个字符串，遍历当前字符串并打印，如果遇见
# “q”,则跳出循环。如果遇见“ ”（空格）则跳过当前输出。

# inp = input('请输入一个字符串：')
# for i in inp:
#     if i=='q':
#         break
#     elif i==' ':
#         continue
#     print(i)

# 使用for循环计算从0到用户输入的值的累加和
inp = input('请输入一个数字')
sum = 0
for i in range(int(inp)+1):
    sum = sum+i
print(sum)