#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  13:51
# !@Author : SweetBeaner
# !@File :.py
# !@Information :标识符与关键字

# 标识符：程序员在程序里面自己定义的名字(变量名、函数名、类名)称为标识符

# 标识符组成：可以有字母、数字、下划线组成，但是不能以数字开头

# 错误写法，变量名不能以数字开头
# 3name = "李四"

# 标识符的命名规则：驼峰命名法和下划线命名法
# 驼峰命名法：
# 1.小驼峰：第一个单词首字母要小写，其它单词首字母要大写，比如：aDog
# 2.大驼峰: 每个单词的首字母都要大写，其它字母要小写，比如: FirstName

# 下划线命名法: 单词之间使用下划线进行分割，单词都要小写，比如： send_message

# 提示：以后使用标识符的时候要注意【见名知意】的特点。

# 虽然可以，但是不建议使用这个变量名，防止和系统的名字重名
int = "a"
print(int)

# 导入模块，通俗理解引入一个python文件，目的使用该文件中的功能代码

import keyword

result = keyword.kwlist
print(result)
print(type(result))
