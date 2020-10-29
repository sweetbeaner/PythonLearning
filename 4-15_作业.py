#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  15:44
# !@Author : Sweetbeaner
# !@File :.py
# !@Information :

# 如果需要使用变量保存以下字符串，我们该如何书写代码
# 鲁迅说:"我没有说过这句话"
# str = '鲁迅说"我没说"'
# # print(str)

# 做一个简单的用户信息管理系统：
# 提示用户依次输入姓名，年龄和爱好
# 并且在输入完成之后，一次性将用户输入的数据展示出来

# name = input('请输入姓名：')
# age = input('请输入年龄：')
# fav = input('请输入爱好：')
# print('姓名为%s;年龄为%s；爱好%s'%(name,age,fav))

# 现有字符串如下，请使用切片提取出ceg
# words = "abcdefghi"
# print(words[2:7:2])

# 题干
# 1，判断单词great是否在这个字符串中，如果在，则将每一个great后面加一个s， 如果不在则输出 great不在该字符串中
# 2，将整个字符串的每一个单词都变成小写，并使每一个单词的首字母变成大写
# 3，去除首尾的空白，并输出处理过后的字符串
# str = '  make American great again  '
# if str.find('great')>0:
#     str = str.replace('great','greats',str.count('great'))
#     print(str)
# else:
#     print('great不在字符串中')
# str = str.upper()
# str = str.lower()
# str = str.title()
#
# str=str.lstrip()
# str=str.rstrip()
# print(str)


# 有一个列表，判断列表中的每一个元素是否以s或e结尾，如果是，则将其放入一个新的列表中，最后输出这个新的列表
# list = ["sed", "apples", "orange", "pink", "bananas", "blue", "black", "white"]
# newList = []
# for value in list:
#     if str(value).startswith('s') or str(value).endswith('e'):
#         newList.append(value)
# print(newList)

# 给定一个列表，首先删除以s开头的元素，删除后，修改第一个元素为"joke"，并且并且把最后一个元素复制一份，放在joke的后边
list = ["spring", "look", "strange" "curious", "black", "hope"]
for value in list:
    if value.startswith('s'):
        list.remove(value)
list[0]='joke'
list.insert(1,list[len(list)-1])
print(list)