import time


def count_time(func):
    def inner():
        print("start")
        start_time = time.time()
        func()
        stop_time = time.time()
        print('end')
        print(f'函数执行时间为{stop_time - start_time}秒')

    return inner


@count_time
def show():
    for i in range(3):
        print(f"sleep")
        time.sleep(1)


if __name__ == '__main__':
    # @count_time
    # def func():
    #    ...

    # show = count_time(show)

    show()

# 结果：
# 第 1 次输出
# 第 2 次输出
# 第 3 次输出
