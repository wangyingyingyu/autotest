"""
间距之和
意给定一个包含表示数字间距的列表nums，其中间距是由2个数字构成的元组对象，并且元组中都按升序排列。
例如:[(1,5)，(6,10)]表示有2个间距，第一个间距是`(1,5)，长度为`5-1=4`。同时，如果多个间距存在交叠，则在计算时应扣除交叠部分长度。
请编写一个函数，计算出列表中所有间距长度的总和。
示例:
输入:`[(1, 5)，(6,10)]`，输出:`8`。
输入:`[(1,4)，(7,10)，(3,5)]`，输出: 7
"""


def c_d(ranges):
    if not ranges:
        return 0

    # 首先对间距按起始位置进行排序
    ranges.sort(key=lambda x: x[0])

    total_length = 0
    current_start, current_end = ranges[0]

    for start, end in ranges[1:]:
        if start > current_end:  # 无重叠
            total_length += current_end - current_start
            current_start, current_end = start, end
        else:  # 存在重叠
            current_end = max(current_end, end)

    # 最后一个范围的长度
    total_length += current_end - current_start

    return total_length


# 测试示例
print(c_d([(1, 5), (6, 10)]))  # 输出: 8
print(c_d([(1, 4), (7, 10), (3, 5)]))  # 输出: 7