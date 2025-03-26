"""
给定一个列表，两个相邻的且相同的数字为一对。
比如给定的列表 a,a,a,b,c,c,d,d,d 中，
 a 有两对，第一个 a 和第二个 a 是一对，第二个 a 和第三个 a 也是一对，所以 a 有两对、c 有一对、d 有两对。求有哪些是成对的，已经有几对？
此时经过你编写的算法应该输出: {'a': 2, 'c': 1, 'd': 2}
"""


def count_pairs(lst):

    pairs_num = {}

    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1]:
            if lst[i] in pairs_num:
                pairs_num[lst[i]] += 1
            else:
                pairs_num[lst[i]] = 1

    return pairs_num
pairs_list = ['a', 'a', 'a', 'b', 'c', 'c', 'd', 'd', 'd']


result = count_pairs(pairs_list)
print(result)






