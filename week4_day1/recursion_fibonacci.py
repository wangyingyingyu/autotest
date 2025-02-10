def fibonacci (n):
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    return fibonacci(n-2) + fibonacci(n-1)
result = fibonacci(8)
print(result)
# 1 1 2 3 5 8 13 21

def f(n):
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        # 获取前 n-1 项的斐波那契数列
        f_list = f(n - 1)
        # 计算第 n 项的值，并添加到列表中
        f_list.append(f_list[-1] + f_list[-2])
        return f_list

# 测试
print(f(5))  # 输出 [1, 1, 2, 3, 5]
import os

# 获取路径分隔符
path_separator = os.sep
print("Path Separator:", path_separator)

