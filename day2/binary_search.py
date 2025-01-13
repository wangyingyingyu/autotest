"""二分查找
编写一个 Python 程序，实现二分查找。
二分查找是一种在有序数组中查找元素的算法。将数组分成两部分，判断目标元素可能在哪一部分。直到找到目标元素或确定目标元素不存在于数组中。
"""
def binary_search(array,num):
    low = 0
    high = len(array)-1
    if low <= high:
        mid = (low+high)//2
        result = array[mid]
        if result == num:
            return result
        elif num > result:
            low = mid + 1
        else:
            high = mid - 1
    else:
        print(f'{num}不存在有序数组中')
if __name__ == '__main__':
    array = [3,5,6,7,8]
    num = 5
    answer = binary_search(array, num)
    print(answer)
"""
在20-90区间内找50  20_____28_____37_____46_____55_____63_____72_____81_____90
整除向下取整  (90-20)//2=35       20+(55-20)//2=37      55+(90-55)//2=72
使用 `while low <= high:` 循环，直到找不到目标数（即 `low` 超过 `high`）。
- 计算中间索引 `mid` 并获取中间元素 `result`。
- 根据当前元素与目标数的比较来决定更新低位或高位索引
"""
















