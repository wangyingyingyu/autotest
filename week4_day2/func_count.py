import time


def count_calls(func):
    count = 0  # 初始化调用次数

    def wrapper(*args, **kwargs):
        nonlocal count  # 允许我们修改外层函数的变量
        count += 1  # 每次调用时增加计数
        print(f"Function '{func.__name__}' has been called {count} times.")  # 打印调用次数
        return func(*args, **kwargs)  # 调用原始函数

    return wrapper  # 返回包装函数


# 示例函数
@count_calls
def example_function(x):
    return x * 2  # 返回 x 的两倍


# 测试代码
if __name__ == "__main__":
    print(example_function(5))  # 第一次调用
    print(example_function(10))  # 第二次调用
    print(example_function(15))  # 第三次调用

"""课堂练习
编写一个 Python 程序，实现一个计数器函数。
该函数能够记录特定函数的调用次数。
需要使用闭包和装饰器来实现这个功能。

7. 编写一个装饰器（40分） log_execution，用于记录函数的执行时间和调用次数。
装饰器应该能够记录每次函数调用的时间、输入参数和返回值，并在函数执行完毕后打印出执行时间和调用次数。
装饰器应该能够应用于任何函数，并在函数执行完毕后打印出调用日志。
"""
# import time
# def log_execution(func):
#     n = 0
#     start_time = time.time()
#     func()
#     end_time = time.time()
#     n += 1
#     return f'执行时间{end_time-start_time},执行次数{n}'
#
# def func1(num):
#     x = num +2
#     return x
# result = log_execution(func1)
# print(result)


from functools import wraps
import time

def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal count
        count = 0

        # 记录开始时间
        start_time = time.time()

        # 调用原始函数并获取返回值
        result = func(*args, **kwargs)

        # 记录结束时间
        end_time = time.time()

        # 更新调用次数
        count += 1

        # 计算执行时间
        execution_time = end_time - start_time

        # 打印日志
        print(f"Function '{func.__name__}' executed!")
        print(f"Input arguments: args={args}, kwargs={kwargs}")
        print(f"Return value: {result}")
        print(f"Execution time: {execution_time:.6f} seconds")
        print(f"Call count: {count}")

        return result

    # 使用 nonlocal 声明来保持一个外层作用域的变量
    count = 0
    return wrapper


# 示例函数
@log_execution
def func1(num):
    x = num + 2
    return x


# 测试代码
if __name__ == "__main__":
    result1 = func1(5)  # 第一次调用
    result2 = func1(10)  # 第二次调用