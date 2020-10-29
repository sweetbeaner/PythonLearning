#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  23:21
# !@Author : Sweetbeaner
# !@File :.py
# !@Information :
# 我想获得“alisi”这个内容，你能否想到三种方法来做？
# typle1 = ("tom", "kaisa", "alisi", "xiaoming", "songshu")
# print(typle1[2])
# print(typle1[2:3])
# for value in typle1:
#     if value == 'alisi':
#         print(value)
#         break


### 题目2（实操题）

#### 题干

# 有如下元组：
# typle1 = ("tom", "kaisa", "alisi", "xiaoming", "songshu")
# str = 'Sweetbeaner1'
# list = ['Sweetbeaner1','Sweetbeaner']
# # 求出他的长度
# print(len(typle1),len(str),len(list))
# list[0]='Tracy'
# print(list[0])
# # typle1[0] = '汤姆'

### 题目3（实操题）
#### 题干

# 现有字典
# dict1 = {'name':'python'}
# # ``，将键为``'name'的值更改为'chuanzhi'``
# dict1['name'] = 'chuanzhi'
# print(dict1['name'])


### 题目4（实操题）

#### 题干

# 现有字典``
# dict1 = {'name': 'chuanzhi', 'age': 18}
# #   要求：1.删除age：18这个键值对
# # ​       2.将整个字典里面的所有键值对，清空
# del dict1['name']
# print(dict1)
# dict1.clear()
# print(dict1)


### 题目5 （实操题）

#### 题干

# 现有字典``
# dict1 = {'name': 'chuanzhi', 'age': 18}
# ``
# 要求：1.使用循环将字典中所有的键输出到屏幕上
# ​    2.使用循环将字典中所有的键输出到屏幕上
# ​    3.使用循环将字典中所有的键值对输出到屏幕上
# ​      输出方式：  name：chuanzhi
# ​                 age:18

# for keys in dict1.keys():
#     print(keys)
# for values in dict1.values():
#     print(values)
# for keys,values in dict1.items():
#     print('%s:%s'%(keys,values))

### 题目6 (实操题)
#### 题干

# 有这样的一个列表
# ```python
# product = [
#     {"name": "电脑", "price": 7000},
#     {"name": "鼠标", "price": 30},
#     {"name": "usb电动小风扇", "price": 20},
#     {"name": "遮阳伞", "price": 50},
# ]
# ```
# 然后小明一共有8000块钱，那么他能不能买下这所有商品？
# 如果能，请输出“能”，否则输出“不能”
# sum = 0
# for prod in product:
#     sum =sum+prod.get('price')
# if sum <= 8000:
#     print('总共花费%d，能'%sum)
# else:
#     print('不能')

### 题目7 （实操题）

#### 题干

# 定义一个简单的函数run，函数的功能是输出"我在跑步" 以及 “管住嘴，迈开腿”，并调用此函数。

def run(i):
    print('%d我在跑步' % i)
    print('管住嘴，迈开腿')


i = 0
for i in range(1000):
    run(i)
    i += 1
