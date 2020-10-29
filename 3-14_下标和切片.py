#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  17:10
# !@Author : SweetBeaner
# !@File :.py
# !@Information :
# 练习：根据下标分别获取第一个数据和最后一个数据

inp = input('输入一个字符串')
print('第一个字符%s,最后一个字符%s,字符串长度%d'%(inp[0],inp[len(inp)-1],len(inp)))

# 练习1：利用切片获取前两个数据
print(inp[0:2])

# 练习2：利用切片获取后两个数据
print(inp[len(inp)-2:len(inp)])

# 练习3：通过切片获取整个字符串
print(inp[0:len(inp)])

# 练习4：通过切片从倒数第一个数据获取到倒数第三个数据
print(inp[len(inp):len(inp)-4:-1])


# 练习5：利用切片让字符串反转的简写方式
print(inp[::-1])