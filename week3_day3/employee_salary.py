"""
实战：员工薪资
设计一个简单员工系统设计，包括不同类型的员工（如全职员工和兼职员工）。每个员工有不同的薪资计算方法。
创建一个 Employee（员工）类，拥有一个抽象方法计算薪资的方法 calculate_salary()。
创建一个 FullTimeEmployee（全职员工）类，继承自 Employee 类，实现 calculate_salary() 方法来计算全职员工的薪资。
创建一个 PartTimeEmployee（兼职员工）类，继承自 Employee 类，实现 calculate_salary() 方法来计算兼职员工的薪资。
实例化一个 FullTimeEmployee 对象，设置工时为 160，时薪为 100，调用 calculate_salary() 方法计算并打印出全职员工的薪资。
实例化一个 PartTimeEmployee 对象，设置工时为 80，时薪为 50，调用 calculate_salary() 方法计算并打印出兼职员工的薪资

"""
class Employee:
    def __init__(self,day_salary, day):
        self.day_salary = day_salary
        self.day = day
    def calculate(self):
        self.salary = self.day_salary*self.day
        return f'全职员工的薪资为{self.salary}'

class FullTimeEmployee(Employee):
    def __init__(self,day_salary, day):
        super().__init__(day_salary, day)
    def calculate(self):
        self.salary = self.day_salary * self.day
        return f'全职员工的薪资为{self.salary}'


class PartTimeEmployee(Employee):
    def __init__(self,day_salary, day):
        super().__init__(day_salary, day)

    def calculate(self):
        self.salary = self.day_salary * self.day
        return f'全职员工的薪资为{self.salary}'



#实例化FullTimeEmployee对象
person1 = FullTimeEmployee(160,100)
print(person1.calculate())


#实例化PartTimeEmployee对象
person2 = PartTimeEmployee(80,50)
print(person2.calculate())







