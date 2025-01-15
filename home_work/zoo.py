"""
课后作业
设计一个简单的动物园系统，其中包含不同类型的动物（如狗、猫和鸟）。
每个动物都有自己的属性（如名字、年龄）和行为（如发出声音）。
使用封装、继承和多态来完成。
"""
class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        return f'{self.name}今年{self.age}岁了'


    def act(self):
        pass
    def eat(self):
        pass


class Bear(Animal):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color = color
    def __str__(self):
        return f'{self.info()}，颜色为{self.color}'
    def act(self):
        return f'{self.name}正在冬眠'

    def eat(self):
        return f'{self.name}喜欢蜂蜜'

class Panda(Animal):
    def __init__(self,name,age,color):
        super().__init__(name, age)
        self.color = color
    def __str__(self):
        return f'{self.info()}，颜色为{self.color}'

    def act(self):
        return f'{self.name}正在翻滚'

    def eat(self):
        return f'{self.name}喜欢竹子'


class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)


    def show_animals(self):
        for animal in self.animals:
            print(animal)
            print(f"{animal.act()}，{animal.eat()}")


if __name__ == "__main__":
    # 创建动物的实例
    bear = Bear('小熊', 7, 'brown')
    panda = Panda('熊猫', 3, 'black-and-write')

    # 创建动物园实例
    zoo = Zoo()

    # 将动物添加到动物园
    zoo.add_animal(bear)
    zoo.add_animal(panda)


    # 展示动物园的动物
    zoo.show_animals()




