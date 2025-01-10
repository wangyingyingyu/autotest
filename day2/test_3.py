
# 初始化变量n_sum为0，用于累计求和。
# 初始化变量n_max和n_min为None，用于保存最大值和最小值。
# 创建一个列表data，其中保存了要处理的数字数据。
# 使用while循环遍历列表data中的每个元素，通过遍历获取每个数字。
# 在循环内部，依次进行以下操作：
# 循环结束后，得到数字的和、最大值和最小值。
# 打印输出数字的和、最大值和最小值。
# 计算平均数

data = [2,4,6, 4]
i = 0
min_data = data[1]
max_data = data[2]
sum_data = 0

while i < len(data):
    num = data[i]
    sum_data += num
    if max_data < data[i]:
        max_data = data[i]
    elif min_data > data[i]:
        min_data = data[i]
    else:
        max_data = max_data

    i += 1

print(sum_data)
print(max_data)
print(min_data)
print(sum_data/len(data))
from random import randint

print(randint(1,10))








