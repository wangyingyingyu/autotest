"""
课堂练习
编写程序，让用户输入两个整数 start 和 end,然后输出这两个整数之间的一个随机数。
要求考虑用户输入不是整数的情况，以及 start>end 的情况。使用异常处理的方式，根据实际情况进行适当提示或输出。
"""
# isdigit() 是 Python 中字符串对象的一个方法，用于检查字符串是否只包含数字字符。
# 如果字符串中的所有字符都是数字（0-9），则返回 True，否则返回 False。
# isdigit() 不能识别负数和小数，因为它们包含非数字字符（- 和 .）。

def random_num():
    start = input("输入开始值：")
    end = input("输入结束值：")

    if not start.isdigit() or not end.isdigit():
        raise Exception("start 和 end 必须是整数")

    elif start > end:
        raise Exception("开始值大于结束值")

    else:
        r = random.randint(int(start), int(end))
        print(f'生成的随机数为：{r}')

try:
    random_num()
except Exception as e:
    print(f"捕获到异常{e}")


import random

def random_num(start, end):
    # 检查 start 和 end 是否为整数
    if not isinstance(start, int) or not isinstance(end, int):
        raise Exception("start 和 end 必须是整数")

    # 检查 start 是否小于 end
    if start >= end:
        raise Exception("开始值必须小于结束值")

    # 生成随机整数
    r = random.randint(start, end)
    return r

# 测试
try:
    result = random_num(3, 6)
    print(f"生成的随机数是: {result}")
except Exception as e:
    print(f"捕获到异常: {e}")
