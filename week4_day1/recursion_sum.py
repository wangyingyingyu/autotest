"""
课堂练习：数组求和
"""
def recursion_sum(arr):

    if not arr:
        return 0
    # 递归情况：列表的第一个元素 + 余下元素的和
    else:
        return arr[0] + recursion_sum(arr[1:])

# 测试
arr = [1, 2, 3, 4, 5]
total_sum = recursion_sum(arr)
print(total_sum)


# 1、五次递归调用 2、递归调用返回结果