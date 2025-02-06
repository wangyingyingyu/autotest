"""
【每日一题】寻找末位偶数
意已知一个由整数组成的列表`nums`假设给定一个长度n，请编写一个函数，在列表中找出位置靠后的n个偶数，并且保持
>示例:
>输入:`([1,2,3,4,5,6,7, 8, 9],3)`,输出:`[4,6,8]`。
"""
def even_number(arr,n):
    even_list = []
    for i in arr:
        if i % 2 == 0 or i == 0:
            even_list.append(i)
    if len(even_list) >= n:
        reverse_even = even_list[::-1]
        return reverse_even[:n][::-1]
    else:
        return f'数列中的偶数个数小于n'


arr = [1,2,3,4,5,6,7, 8, 9]
print(even_number(arr,3))


def find_last_n_even(nums, n):
    # 结果列表
    result = []

    # 从末尾向前遍历
    for num in reversed(nums):
        if num % 2 == 0:             # 检查是否为偶数
            result.append(num)
        if len(result) == n:         # 达到 n 个偶数时停止
            break

    # 由于我们是从后往前遍历的，结果需反转以恢复原顺序
    return list(reversed(result))


# 示例输入
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 3
even = find_last_n_even(nums, n)
print(even)







