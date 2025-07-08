# 编写一个装饰器 log_execution，用于记录函数的执行时间和调用次数。
# 装饰器应该能够记录每次函数调用的时间、输入参数和返回值，并在函数执行完毕后打印出执行时间和调用次数。
# 装饰器应该能够应用于任何函数，并在函数执行完毕后打印出调用日志。
import time
def log_execution(example):

    count = 0
    def wrapper():
        nonlocal count
        start_time = time.time()
        example()
        end_time = time.time()
        e_time = end_time-start_time
        count += 1
        print(f'函数{example.__name__}的执行时间为{e_time},执行次数为{count}')
    return wrapper


@log_execution
def func():
    time.sleep(1)


print(func())
