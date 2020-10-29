#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  23:02
# !@Author : Sweetbeaner
# !@File :.py
# !@Information :

# 练习1: + 完成两个列表的合并
list1 = ['1','2','3']
list2 = ['a','b','c']
print(list1+list2)
# 练习2: * 完成字符串的数据复制成3份
str = 'ok'
print(str*3)
# 练习3：使用in判断字典中是否有张三这个值

dict = {'张三':'姓名','年龄':18}
if '张三' in dict:
    print('有张三',dict['张三'])
else:
    print('没张三')
