"""
封装
"""
class A(object):
    def __init__(self):
        # 公有属性
        self.a = 10
        # 保护属性
        self._b = 20
        # 私有属性
        self.__c = 30
    # 公有方法
    def show(self):
        # 在类中使用公有属性
        print(f"A: {self.a}")
        # 在类中使用保护属性
        print(f"B: {self._b}")
        # 在类中使用私有属性
        print(f"C: {self.__c}")
        # 在类中使用保护权限的方法
        self._display()
        # 在类的内部调用私有方法
        self.__privacy()

    # 保护权限的方法
    def _display(self):
        print(f"B: {self._b}")
    # 私有方法
    def __privacy(self):
        print(f"A: {self.__c}")

#子类重写父类的方法
class A(object):
    # A 继承自 object 根类
    def show(self):
        print("父类A的方法")

class B(A):
    # 子类重写父类方法
    def show(self):
        print("子类B的方法")

b = B()
# 当子类方法与父类方法同名时，调用子类方法，显示子类重写后的方法
b.show()

class A(object):
    # A 继承自 object 根类
    def __init__(self, a):
        self.a = a


class B(A):
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b

b = B("A","B")
print(b.a)
print(b.b)
# 父类中所有的私有属性和方法，子类不能直接继承，只能将父类的私有属性
























