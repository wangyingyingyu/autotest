# 实战：选择排序
#对于要排序的数组，第 1 轮比较将找出此时数组中最小的数字。
#找到后将该数字与第 1 个数字交换，此时称一个数字已被排序。然后开始第2轮比较，重复上述过程。
#每一轮的比较将使得当前未排序数字中的最小者被排序，未排序数字总数减 1。第 arr.length−1 轮结束后排序完成。
from day2.test_1 import result


def select_sort(arr):
    l = len(arr)  # 获取数组长度
    for i in range(l - 1):       # 外层循环，进行 l-1 次
        minimum_index = i        # 假设当前未排序部分的第 i 个元素是最小值的索引
        for j in range(i + 1, l):       # 内层循环，查找未排序部分的最小值
            if arr[j] < arr[minimum_index]:          # 如果发现更小的元素
                minimum_index = j       # 更新最小值的索引
        # 交换找到的最小值与当前第 i 个元素
        arr[i], arr[minimum_index] = arr[minimum_index], arr[i]

    return arr          # 返回排序后的数组

if __name__ == '__main__':
    arr = [4, 5, 7, 2, 1]
    sorted_arr = select_sort(arr)
    print(sorted_arr)
# 遍历第i位数后面的未排序列表和第i位数比较，找到最小值，并设置最小值索引为j交换第i位数和第j位数（最小值）
"""第一轮： i=0 min=0 j=1 5>4 不符合判断条件 进入下一个内循环
              min=0 j=2 7>4 不符合判断条件 进入下一个内循环
              min=0 j=3 2<4 符合判断条件 执行if循环语句 min=j=3 进入下一个内循环  此时最小值索引为3，最小值为2
              min=3 j=4 1<2 符合判断条件 执行if循环语句 min=j=4 进入下一个内循环  此时最小值索引为4，最小值为1
              min=1 内循环遍历完成 执行外循环最后一条语句 将最小值和第一位数位置调换 进入下一个外循环
    第二轮： i=1          

"""
def select_sort():
    data = [1,56,6,5,4,89,2]
    length = len(data)
    for i in range(length-1):
        for j in range(i+1,length):
            small = data[i]
            if data[j]<small:
                data[i],data[j] = data[j],data[i]
    return data

result = select_sort()
print(result)
"""
i=0 j=1 small=1 56>1 执行下一次内循环
    j=2 small=1 6>1 执行下一次内循环
    ……
    j=6 small=1 2<1 执行下一次内循环 1,56,6,5,4,89,2
i=1 j=2 small=56 6<56 符合if循环条件 交换索引值为i和j数值的顺序1,6,56,5,4,89,2 执行下一次内循环
    j=3 small=6  5<6 符合循环条件 交换索引值为i和j数值的顺序 1,5,56,6,4,89,2 执行下一次内循环
    j=4 small=5  4<5 符合循环条件 交换索引值为i和j数值的顺序 1,4,56,6,5,89,2 执行下一次循环
    j=5 small=4  89>4 不符合if循环条件 执行下一次内循环 1,4,56,6,5,89,2
    j=6 small=4  2<4 符合if循环条件 交换索引值为i和j数值的顺序  1,2,56,6,5,89,4 执行下一次循环

"""

