# 实战：冒泡排序
#对于要排序的数组，从第一位开始从前往后比较相邻两个数字，若前者大，则交换两数字位置，然后比较位向右移动一位。
"""
def bubble():
    n = [2,3,1,6,4]
    l = len(n)
    for i in range(l-1):
        for j in range(l - 1):
            if n[j] > n[j+1]:
                n[j],n[j+1] = n[j+1],n[j]

    return n

bubble_sort = bubble()

print(bubble_sort)


def Bubble():
    n = [2,3,1,6,4]
    l = len(n)
    i= 0

    while i < l-1:
        j = 0
        while j <l-1:
            if n[j] > n[j + 1]:
                n[j], n[j + 1] = n[j + 1], n[j]
            j+=1
        i+=1

    return n

Bubble_sort = Bubble()
print(Bubble_sort)

"""
def bubble_sort(arr):   # 定义泡沫排序函数，接收一个列表arr作为参数
    for i in range(len(arr)-1):   # 外层循环，表示需要进行n-1轮比较，也就是len(arr)-1次
        swap = False    # 初始化一个开关，表示这一轮是否发生了交换
        for j in range(len(arr)-1-i):# 内层循环运行len(arr)-1-i次，这是因为每进行一轮排序，最后的元素已经被排好，不需要再比较。
            # 内层循环，比较相邻的两个元素
            if arr[j] > arr[j + 1]:   # 如果当前元素大于下一个元素
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # 交换这两个元素
                print(f'交换后的数组状态：{j}:{arr}')
                swap = True  # 发生交换，标记swap为True
        if not swap:  # 如果这一轮没有发生任何交换
            break  # 提前终止循环，有序，代码不需要再次执行其他比较
    return arr  # 返回排序后的数组

if __name__ == '__main__':  # 当脚本作为主程序执行时
    arr = [4, 5, 7, 2, 1]  # 初始化一个无序数组
    print(bubble_sort(arr))

"""
i=0 j=0 4<5 不符合if判断条件 执行下一次内循环  [4, 5, 7, 2, 1] swap=False
    j=1 5<7 不符合if判断条件 执行下一次内循环  [4, 5, 7, 2, 1]
    j=2 7>2 符合if判断语句 交换索引为2、3两个元素的位置 swap=True 执行下一次内循环 [4, 5, 2, 7, 1]
    j=3 7>1 符合if判断语句 交换索引值为3、4两个元素的位置 swap=True 执行下一次内循环 [4, 5, 2, 1, 7]
    j取值完毕 执行下一次外循环 最大值 ‘7’ 已经排好，只需给未排序的前len(arr)-1-i列排序
i=1 j=0 4<5 不符合if判断条件 执行下一次内循环
    j=1 5>2 符合if判断条件 交换索引值为1、2两个元素的位置 swap=True 执行下一次内循环
    

    
"""


