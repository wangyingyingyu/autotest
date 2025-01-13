# 函数返回值
"""
def show():
    print("循环前输出内容")
    for i in range(10):
        print(i)
        if i == 2:
            return
    print("循环后输出内容")

print("函数调用前输出内容")
show()
print("函数调用后输出内容")


def getTwoNum():
    a = int(input("请输入第一个数字："))
    b = int(input("请输入第二个数字："))
    return a, b

result = getTwoNum()
print(result)
print(type(result))




# 调用两个返回值 返回一个元组
def getTwonum ():

    a = int(input("输入第一个值：\n"))
    b = int(input("输入第二个值: \n"))
    return a, b

result = getTwonum()
# num1,num2 = getTwonum()
print(result)

# 函数位置传参，关键字参数显式指定形参名字，将值赋值给形参 默认值参数

# 可变位置*args参数
def get_sum(*args):
    '''
    不确定数字求和
    :param args:接收不确定个数的位置参数, *args 将接收到的任意多个实际参数放到一个元组中。
    :return:
    '''
    print(*args)
    print(args)
    print(type(*args))
    print(type(args))
    sum = 0
    for i in args:
        sum += i
    print(sum)
    print('*'*10)

get_sum(0,9,8)
#get_sum(2,2,2)

#  **kwargs 必须遍历字典里的键值对，才能将不确定的关键字参数中的关键字参数打印出来




# 全局变量定义
m = 10
def show():
    # 局部变量与全局变量同名
    global m
    m = "ABC"
    # 使用局部变量
    print("show:", m)

# 使用全局变量
print(m)
show()
# 使用全局变量
print(m)



def computer(nums):
    data = nums
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

    print(f'求和：{sum_data}')
    print(f'最大值：{max_data}')
    print(f'最小值：{min_data}')
    print(f'平均值：{sum_data / len(data)}')

nums = [12,34,3,6,56,33434,6,3,23,23,23,57,78,11,1,8,9]
computer(nums)



# 从键盘输入一个字符序列，统计，大写字母，小写字母，数字，其它字符各出现次数，将次数保存到字典中
def countABC():
    strs = input("输入一个字符序列：")
    new_strs = strs.split()
    dic = {
        "大写字母出现次数": 0,
        "小写字母出现的次数": 0,
        "数字出现的次数": 0,
        "其他字符出现的次数": 0
    }
    # dic = {}
    for i in strs:
        if i.isupper() == True:
            dic["大写字母出现次数"] += 1
        else:
            if i.isdigit() == True:
                dic["数字出现的次数"] += 1
            else:
                if i.islower() == True:
                    dic["小写字母出现的次数"] += 1
                else:
                    dic["其他字符出现的次数"] += 1

    print(dic.items())


countABC()

"""



# 九九乘法表
def computer():
    i = 1
    while i <= 9:
        j = 1
        while j <= i:
            print(f'{j}*{i} = {i * j}', end=" ")
            j += 1
        print('\t')
        i += 1


computer()

def computer_1():
    for i in range(1,9):
        for j in range(1, i+1):
            print(f'{j}*{i} = {i * j:<2}', end=" ")# 输出二宽度的数并且左对齐
        print()
computer_1()


import math

m = int(input("请输入一个正整数："))
n = int(math.sqrt(m)) # int()向下取整
for i in range(2, n + 2):
    if m % i == 0:
        # print(f'{i}不是素数')
        break  # 可以整除，肯定不是素数，结束循环
if i == n + 1:
    print(m, "是素数！")
else:
    print(m, "不是素数")


import math

# 用户输入正整数
num = int(input("请输入一个正整数："))

# 判断是否为素数
def is_prime(n):
    if n <= 1:
        return False
    import math

# 用户输入正整数
num = int(input("请输入一个正整数："))

# 判断是否为素数
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# 输出结果
if is_prime(num):
    print(f"{num} 是素数")
else:
    print(f"{num} 不是素数")


# ### 3. **埃拉托斯特尼筛法**
# 这是一种有效地找出小于某个数 \( n \) 的所有素数的方法：
# 1. 创建一个大小为 \( n \) 的布尔数组，每个元素初始为 `True`（即假设所有数字都是素数）。
# 2. 从第一个素数（2）开始，将其所有倍数标记为 `False`。
# 3. 对下一个 `True` 的数重复此过程，直到处理到 \( \sqrt{n} \)。
# 4. 剩下的标记为 `True` 的数即为素数


m = int(input("请输入一个正整数："))
if m <= 1:
    print(f'{m}不是素数')

elif m == 2:
    print(f'{m}是素数')
else:
    for i in range(2, m):
        if m % i == 0:

            break  # 可以整除，肯定不是素数，结束循环
            print(f'{m}不是素数')
        else:
            print(f"{m}是素数")



def prime_num(m):
    if m <= 1:
        print(f'{m}不是素数')

    elif m == 2:
        print(f'{m}是素数')
    else:
        for i in range(2, m):
            if m % i == 0:
                return False
            return True

def is_prime(m):
    if prime_num(m):
        print(f'{m}不是素数')
    else:
        print(f"{m}是素数")

is_prime(9)

# 实战：水仙花数
# 编写一个 Python 程序，找出 100-999 范围内的水仙花数。
# 所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
# 例如：153 是一个"水仙花数"，因为 153=1^3＋5^3＋3^3

def flower():
    for i in range(100,1000):
        a = i%10
        b = (i%100) // 10
        c = i // 100
        if i == a**3 + b**3 + c**3:
            print(i)

flower()








