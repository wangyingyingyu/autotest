"""
给定2个数字列表，请编写一个函数，当它们至少拥有1个相同元素时返回 True:否则返回 False。
示例:
输入`[9,8, 7]，[8,1, 3」，输出:True。
"""

def different (arr1, arr2):
    for i in arr1:
        for j in  arr2:
            if i == j:
                return  True

    return False




arr1 = [9,8, 7]
arr2 = [0,1, 7]

print(different(arr1,arr2))



def element(list1, list2):
    # 将列表转换为集合
    set1 = set(list1)
    set2 = set(list2)

    # 检查两个集合是否有交集
    return not set1.isdisjoint(set2)


# 示例
list1 = [9, 8, 7]
list2 = [8, 1, 3]
result = element(list1, list2)
print(result)