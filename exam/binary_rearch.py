
def binary_search(array,num):
    low = 0
    high = len(array)-1
    while low <= high:
        mid = (low+high)//2
        result = array[mid]
        if result == num:
            return result
        elif num > result:
            low = mid + 1
        else:
            high = mid - 1

    print(f'{num}不存在有序数组中')
if __name__ == '__main__':
    array = [3,5,6,7,8]
    num = 5
    answer = binary_search(array, num)
    print(answer)