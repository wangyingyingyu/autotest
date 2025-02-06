"""
给定一个包含两个正数的列表nums请编写一个函数，将它们首音互换，并且计算他们能之间的差值的绝对值。
备注:首音互换是指将两个对象的第一个元素进行对换例如‘123’ ‘456’
互换后变成、423'和`156`
示例
输入:[123,456]，输出:267 因为423-156=267`
"""


def swap_num(nums):
    if len(nums) != 2:
        raise ValueError("输入的列表应该包含两个正数")

    # 获取两个数字
    num1, num2 = str(nums[0]), str(nums[1])

    # 将两个字符串的首音（首位数字）互换
    swapped_num1 = num2[0] + num1[1:]
    swapped_num2 = num1[0] + num2[1:]

    # 将互换后得到的字符串转换回整数
    swapped_num1 = int(swapped_num1)
    swapped_num2 = int(swapped_num2)

    # 计算差值的绝对值
    difference = abs(swapped_num1 - swapped_num2)

    return difference


# 测试示例
print(swap_num([123, 456]))  