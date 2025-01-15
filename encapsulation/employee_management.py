"""
实战代码
创建 Employee 基类，包含属性 name、age 和 salary，以及一个通用的 work 方法。
创建 Manager 子类，继承 Employee，增加管理团队的方法。
创建 Developer 子类，继承 Employee，增加编程语言属性及展示语言的方法。
使用这些类完成员工的分类管理与信息展示。
"""
#使用 `super()` 时，不需要再将 `self` 作为第一个参数传递

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def work(self):
        return f'上下班打卡'

class Manager(Employee):
    def __init__(self, name, age, salary):
        # Employee.__init__(self, name, age, salary)
        super().__init__(name,age,salary)
    def manage(self):
        super().work()
        return f'管理团队'

class Developer(Employee):
    def __init__(self, name, age, salary,language):
        super().__init__(name, age, salary)
        self.language = language
    def show(self):
        super().work()
        return f'展示{self.language}语言'
person = Employee('姓名','年龄','薪水')
print(person.work())

person1 = Manager('Eve','30','3w')
print(person1.work())
print(person1.manage())

person2 = Developer('Tom','25','2w','python')
print(person2.work())
print(person2.work())
print(person2.show())



