#!/usr/bin/env python
# !-*-coding:utf-8 -*-
# !time :  14:18
# !@Author : Sweetbeaner
# !@File :.py
# !@Information :
# 练习：验证不可变类型的数据是否不能在原有内存空
# 间的基础上修改数据，修改后是否内存地址发生变化


my_int = 30
print(my_int, id(my_int))

# my_int[0] = 4
# 对于不可变类型来说，不能再自身内存地址的基础上修改数据，想要修改数据都要重新赋值
my_int = 40
print(my_int, id(my_int))


my_tuple = (3, 5)

print(my_tuple, id(my_tuple))

# my_tuple[1] = 10
# 想要修改数据都要重新赋值，这样变量保存的内存地址会发生变化
my_tuple = (3, 10)
print(my_tuple, id(my_tuple))
print("=====")
my_str = "abc"

print(my_str, id(my_str))
# my_str[1] = 'd'

my_str = "adc"
print(my_str, id(my_int))

# 总结：
# 不可变类型不能再自身内地地址的基础上修改数据，想要修改数据需要修改变量的引用
# 也就是说修改变量保存的内存地址，重新赋值来完成。

print("=====")
my_str = "abc"
print(my_str, id(my_str))

result = my_str.replace("b", "d")
print("返回的数据为：", result, id(result))

print(my_str, id(my_str))