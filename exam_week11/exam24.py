# 请编写一个选择排序算法
def select_sort():
    data = [1,56,6,5,4,89,2]
    length = len(data)
    for i in range(length-1):
        for j in range(i+1,length):
            small = data[i]
            if data[j]<small:
                data[i],data[j] = data[j],data[i]
    return data

result = select_sort()
print(result)