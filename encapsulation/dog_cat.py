"""
创建一个基础类 Animal，实现通用的属性和方法。
创建派生类 Dog 和 Cat，继承自 Animal 并增加各自的独特行为。
"""
class Animal:
    def __init__(self, name, age,color):
        self.name = name
        self.age = age
        self.color = color
    def play(self):
        return f'play with human'

class Dog(Animal):
    def __init__(self, name, age,color, speak):
        super().__init__(name, age,color)
        self.speak = speak

    def __str__(self):
        return f'Dog(name={self.name}, age={self.age}, color={self.color}, speak={self.speak})'

    def eat(self, food):
        super().play()
        self.food = food
        return f'dog喜欢吃{food}'

class Cat(Animal):
    def __init__(self, name, age,color, speak):
        super().__init__(name, age,color)
        self.speak = speak

    def __str__(self):
        return f'Cat(name={self.name}, age={self.age}, color={self.color}, speak={self.speak})'
    def eat(self, food):
        super().play()
        self.food = food
        return f'cat喜欢吃 {food}'



dog1 = Dog('wangcai','5','black','wangwang')
print(dog1)
print(dog1.play())
print(dog1.eat('bone'))
cat1 = Cat('xiaomi','3','write','miaomiao')
print(cat1)
print(cat1.play())
print(cat1.eat('fish'))














