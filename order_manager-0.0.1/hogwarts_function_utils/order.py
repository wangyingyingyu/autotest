import functools
from time import time


def closure_create(func):
    """
    闭包函数，返回一个函数
    :param func:
    :return:
    """

    def inner():
        print(f'start {time()}')
        func()
        print(f'end {time()}')

    return inner


@closure_create
def save_order():
    """
    输入订单，保存到文件
    :param id:
    :return:
    """
    ...


@closure_create
def read_orders():
    """
    读取文件，判断文件师傅存在
    如果文件存在，返回内容
    :return:
    """


def run():
    """
    给用户一个输出菜单
    :return:
    """

    while True:
        r = int(input("""
        1. read orders
        2. save order
"""))
        print(r)
        if r == 1:
            read_orders()
        elif r == 2:
            save_order()


def repeat(**kwargs):
    """
    @repeat(5) = @decorator_repeat

    :param num_times:
    :return:
    """

    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value

        return wrapper_repeat

    return decorator_repeat


def wrapper_repeat(a=1):
    print(a)


if __name__ == '__main__':
    f()
