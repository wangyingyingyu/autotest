# 编写一个冒泡排序算法，要求能进行正序和反序
def bubble_sort(arr):
    l = len(arr)
    for i in range(l-1):
        for j in range(l-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j]
    return arr,arr[::-1]
if __name__ == "__main__":
    arr = [7,4,6,3,1]
    print(f'冒泡排序正序和反序{bubble_sort(arr)},{bubble_sort(arr)}')