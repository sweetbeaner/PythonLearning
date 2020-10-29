#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  16:29
# !@Author : SweetBeaner
# !@File :.py
# !@Information :
# 练习1: 利用while循环生成1-5的数据，当生成的数据等于3的时候让循环执行结束

i=1
while i<=5:
    print(i)
    if i==3:
        break
    i+=1

# 练习2：利用for循环生成1-5的数据，当生成的数据等于3的时候跳过这个数据，然后打印下一个数据
for i in range(1,6):
    if i==3:
        continue
    print(i)
