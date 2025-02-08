def outer(arg1, arg2):
    outer_a = arg1
    outer_b = arg2

    def inner(x, y=1):
        m = 1
        n = outer_b + m

        print(n)
        return n

    return inner


def run():
    inner = outer(1, 2)
    r = inner(3, 4)
    print(r)



if __name__ == '__main__':
    run()
    print('aaa')
