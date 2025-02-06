"""
【每日一题】手串计数
已知一个手串是由红色和蓝色珠子搭配构成的，并且每两个蓝色珠子之间夹着连续的2个红色珠子。

请编写一个函数，输入一个蓝色珠子的数量num，请求出红色珠子的个数。如果输入的数字小于2则返回 0.
示例:
输入:1，输出:0。
输入:5，输出:8。
"""

def calculate_red_beads(num):
    # 如果输入的数字小于 2，则返回 0
    if num < 2:
        return 0
    # 计算红色珠子的数量
    red_count = num * 2 + 2
    return red_count

# 测试示例
print(calculate_red_beads(1))  # 输出: 0
print(calculate_red_beads(5))  # 输出: 8














