
"""
课堂练习：使用 for 计算列表中元素的平方
给定一个整数列表 [1, 2, 3, 4, 5]，使用 for 循环计算每个数的平方，并将结果存储到新的列表中，最后输出新列表。
"""
list = [1,2,3,4,5]
list_new = []
for i in list:
    num = i ** 2
    list_new.append(num)
print(list_new)
import math

# 计算平方根
number = 25
sqrt_value = []
sqrt_value.append(math.sqrt(number))
print("平方根:", sqrt_value)
