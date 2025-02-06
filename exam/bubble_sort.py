def bubble_sort(arr):

    l = len(arr)
    for i in range(l-1):
        for j in range(l-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

    return f'排序后的数列为：{arr}, 逆序为：{arr[::-1]}'

arr = [3,8,5,9,7,1]
print(bubble_sort(arr))