"""
from datetime import datetime

# 定义一个工具类
class Uitls:
    now = datetime.now()

    @classmethod
    def current_datetime(cls):
        return cls.now


    @classmethod
    def current_date(cls):
        '''
        获取当前的年月日
        :return:
        '''
        return cls.now.strftime("%Y-%m-%d")

    @classmethod
    def current_day(cls):
        '''
        获取当前的天
        :return:
        '''
        return cls.now.day

    @classmethod
    def current_time(cls):
        '''
        获取当前的时间
        :return:
        '''
        return cls.now.strftime("%Y-%m-%d")
print(Uitls.current_datetime())

#静态方法
class Calculate:
    @staticmethod
    def sub(num1,num2):
        return num1+num2

print(Calculate.sub(8,9))

class geometry:
    @staticmethod
    def area(lengh,width):
        return lengh*width

    @staticmethod
    def perimeter(length,width):
        return (length+width)*2


print(geometry.area(2,3))
print(geometry.perimeter(2,3))

# 中医
class Father:
    def cure(self):
        print("使用中医方法进行治疗。。。")

# 西医
class Son(Father):
    def cure(self):
        print("使用西医方法进行治疗。。。")

# 兽医
class AnimalDoctor:
    def cure(self):
        print("使用兽医方法进行治疗。。。")

# 患者
class Patient:
    def needDoctor(self, doctor):
        doctor.cure()


if __name__ == '__main__':
    oldDoctor = Father()
    littleDoctor = Son()
    animalDoctor = AnimalDoctor()

    patient = Patient()

    patient.needDoctor(oldDoctor)
    patient.needDoctor(littleDoctor)
    patient.needDoctor(animalDoctor)

class Student:

    def select_course(self, course_name):
        # 定义选课列表
        courses = []
        courses.append(course_name)
        print(courses)

s1 = Student()
s1.name = "Tom"
s1.age = 22
s1.select_course("Python")
s1.select_course("Java")

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
        # 在类中使用私有方法
        self.__info()


    # 保护权限的方法
    def _display(self):
        print(f"B: {self._b}")

    # 私有权限的方法
    def __info(self):
        # 在类中使用私有属性
        print(self.__c)
obj = A()
# 在类外使用公有属性
print(obj.a)
# 在类外无法使用保护仅限的属性（不建议这样使用）
print(obj._b)
# 在类外使用私有属性，访问失败
# print(obj.__c)
# 在类外使用公有方法
obj.show()
# 在类外无法使用保护权限的方法（不建议这样使用）
obj._display()
# 在类外访问私有方法，访问失败
# obj.__info()
"""

class Father:
    def cure(self):
        print("使用中医方法进行治疗。。。")

# 西医
class Son(Father):
    def cure(self):
        print("使用西医方法进行治疗。。。")


# 患者
class Patient:
    def need_doctor(self, doctor):
        doctor.cure()


if __name__ == '__main__':
    old_doctor = Father()
    little_doctor = Son()

    patient = Patient()
    patient.need_doctor(old_doctor)
    patient.need_doctor(little_doctor)

#
