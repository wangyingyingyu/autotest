# 编写一个 Python 程序，接收一个包含整数的列表，按照从大到小的顺序排序并输出。
def select_sort():
    data = [1,56,6,5,4,89,2]
    length = len(data)
    for i in range(length-1):
        for j in range(i+1,length):
            small = data[i]
            if data[j]<small:
                data[i],data[j] = data[j],data[i]
    return data[::-1]

result = select_sort()
print(result)