"""
课后作业
编写一个函数，使用冒泡排序算法对一个整数列表进行排序。
支持从小到大或从大到小排序。
打印出排序过程中每一轮比较后的列表状态，以便理解冒泡排序的过程。
统计排序过程中总的交换次数并打印。
在主程序中，接收用户输入的多个整数，并调用排序函数进行排序。 最后打印排序后的结果
"""
def bubble_sort(array):
    l = len(array)
    c = 0
    for i in range(l-1):
        for j in range(l-1-i):

            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
                c += 1
                print(f'排序后整数列表为{array}')
        print(f'统计排序过程中交换了{c}次')
    return array


if __name__ == '__main__':
    array = [4, 5, 7, 2, 1]
    print(bubble_sort(array))



















