"""
给定一个3位数的数字，请编写一个函数，将它重新排列，并找出其中值最大的形式。
示例:输入 213 输出 321
"""


def largest_permutation(num):
    # 将数字转换为字符串，然后转换为字符列表
    digits = list(str(num))

    # 使用sorted函数对字符列表进行降序排序
    sorted_digits = sorted(digits, reverse=True)

    # 将排序后的字符列表合并为字符串，并转换回整数
    largest_num = int(''.join(sorted_digits))

    return largest_num


# 测试示例
print(largest_permutation(213))  # 输出: 321