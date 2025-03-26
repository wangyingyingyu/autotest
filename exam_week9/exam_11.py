# 请编写一个冒泡排序算法，编写完成的代码打包成zip文件后上传答题
def bubble_sort(arr):
    swap = False
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            # 内层循环，比较相邻的两个元素
            if arr[j] > arr[j + 1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]# 交换这两个元素
                print(f'交换后的数组状态：{j}:{arr}')
                swap = True
        if not swap:
            break
    return arr

if __name__ == '__main__':

    arr = [4,5,2,7,1]
    print(bubble_sort(arr))















