"""
【每日一题】最大年龄
意 已知一个包含表示年龄的数字列表，它至少会包含2个元素，并且是无序的。请编写一个函数，返回其中最大的两个年龄列表，并按照升序排序
示例:输入:[1,3,10,0]，返回:[3,10]
"""
def sort_age(age_arr):
    l = len(age_arr)
    for i in range(l-1):
        for j in range(l-1-i):
            if age_arr[j]<age_arr[j+1]:
                age_arr[j],age_arr[j+1] = age_arr[j+1],age_arr[j]

    return age_arr[:2][::-1]

age_arr = [1,3,10,0]
print(sort_age(age_arr))







