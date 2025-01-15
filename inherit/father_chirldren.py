# 当子类和父类方法重名时，调用子类的方法，如果这时还想要调用父类中的方法，使用super().父类方法名

class A(object):
    # A 继承自 object 根类
    def show(self):
        print("父类A的方法")

class B(A):
    # 子类重写父类方法
    def show(self):
        # 调用父类的方法
        super().show()
        print("子类B的方法")

b = B()
# 当子类方法与父类方法同名时，调用子类方法
b.show()
# 在子类对象初始化时，需要给出父类初始化的参数，然后使用super().__init__(父类对象初始化时定义的参数)初始化方法初始化父类实例对象的属性
class A:
    def __init__(self,name):
        self.name = name
        print(name)
class B(A):
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age
        print(age)

a = A('Tom')
b = B('Eve',18)

# 在子类中初始化父类的一个私有属性这是不可能实现的，子类可以调用父类初始化方法对父类的私有属性进行初始化
class A1:
    def __init__(self,name):
        self.__name = name

    def show(self):
        print(f'名字为{self.__name}')
class B1(A1):
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age

    def show(self):
        super().show()
        print(f'年龄为{self.age}')

b1 = B1('qiqi',10)
b1.show()


# 多继承初始化
# 由于有多个父类，每个父类的属性都需要单独初始化，这时super（）函数只能引用继承书写顺序的第一个父类，
# 其他的父类无法通过super().__init__(父类参数)引用的，所以无法利用super()函数对父类属性进行初始化
# 此时，可以使用直接指定父类名的方式调用父类初始化属性时的方法,同时给出父类初始化的参数
class A2:
    def __init__(self,name):
        self.name = name

class B2:
    def __init__(self,age):
        self.age = age


class C(B2,A2):
     def __init__(self,name,age,work):
         A2.__init__(self,name)
         B2.__init__(self,age)
         self.work = work
         print(name,age,work)

     def show(self):
        print(f'name"{self.name},age:{self.age},work:{self.work}')

c = C('peiqi',3,'play')
c.show()