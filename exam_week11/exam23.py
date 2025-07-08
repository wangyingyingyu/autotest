# 编写一个二分查找的算法
def binary_search(arr,num):
    l = len(arr)

    high = l-1
    low = 0
    while high >= low:
        mid = (high+low) // 2
        if arr[mid] == num:
            return f'二分法查找元素的位置下标{mid}'
        elif arr[mid] > num:
            high = mid-1
        else:
            low=mid+1
    return '未找到元素'
if __name__ == '__main__':

    arr1 = [1,4,5,7,9,10,13,19]
    num1 = 5
    print(binary_search(arr1,num1))




