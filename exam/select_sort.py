def select_sort(arr):

    l = len(arr)
    for i in range(l-1):
        for j in range(i+1,l-1):
            small = arr[i]
            if arr[j] > small:
                arr[j],arr[i] = arr[i],arr[j]

    return f'排序后的数列为：{arr}'

arr = [3,8,5,9,7,1]
print(select_sort(arr))






