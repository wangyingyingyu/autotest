class Computer:
    count = 0
    def __init__(self):
        Computer.count +=1
        print(f'创建对象的数量：{Computer.count}')

    @classmethod
    def get_count_num(cls):
        return cls.count

    @classmethod
    def motify(cls):
        cls.count = 0
        return cls.count

test1 = Computer()
test2 = Computer()
print(Computer.motify())















