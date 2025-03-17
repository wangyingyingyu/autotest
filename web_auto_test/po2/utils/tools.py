def gen_phone():
    import random
    # 定义范围
    start = 17811110001
    end = 17811119999
    # 生成随机整数
    random_number = random.randint(start, end)
    # 输出结果
    return str(random_number)