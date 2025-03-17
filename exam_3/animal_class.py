# 设计一个动物类系统
#
# 基类 Animal 包含动物的名称和一个抽象方法 speak()，
# 子类 Dog 和 Cat 分别表示狗和猫类，每个子类需要实现 speak() 方法，
# 输出该动物特有的叫声。
# 请使用适当的面向对象特性来实现该系统，使其能够支持不同动物的多态行为。

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self, sound):
        return f'{self.name}叫声为{sound}'

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self, sound):
        return super().speak(sound)

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self, sound):
        return super().speak(sound)

dog1 = Dog("旺财")
print(dog1.speak("汪汪"))

cat1 = Cat("咪咪")
print(cat1.speak("喵喵"))