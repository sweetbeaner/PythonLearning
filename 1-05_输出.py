#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  14:00
# !@Author : SweetBeaner
# !@File :.py
# !@Information :输出

# 控制台输出
print("hello python")

# 换行符
print("hello \nworld")

# 多组数据
name = "SweetBeaner"
age = 30
print(name, age)

# 控制填输出分隔符 sep=""
print(name, age, sep="*")

# 控制输出完成后追加的内容 end=""，默认追加为\n
print(name, age, end="哈哈哈")
print("测试")

# 字符串格式化输出：把字符串里面的动态数据按照指定的数据类型进行输出显示

# 常用的格式化占位符:
# %d 表示格式化输出一个int类型的数据
# %f 表示格式化输出一个float类型的数据
# %s 表示格式化输出一个str类型(字符串)的数据

intro = "我叫%s，很高兴认识你" % name
print(intro)

longIntro = "我叫%s，今年%d岁，很高兴认识你" % (name, age)
print(longIntro)

# float默认保留六位小数
pi = 3.14
print("圆周率:%f" % pi)

# 设置保留具体位小数
print("一位小数:%.1f" % pi)
print("两位小数:%.2f" % pi)

# 格式化占位符，结合百分号，多敲一个
print("离职率:%d%%" % 99)
