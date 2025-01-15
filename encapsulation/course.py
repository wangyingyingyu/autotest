"""
实战代码
创建一个 Course 类表示课程，定义私有属性 __name 和 __credit。
提供封装方法，用于设置和获取课程名称及学分。
模拟一个课程管理系统，支持课程的添加、删除和查看（课程对象）
"""
# 创建Course类
class Course:
    # 定义私有属性
    def __init__(self):
        self.__name = ''
        self.__credit = 0

# 设置课程名称与学分
    def set_course_name(self,course):
        self.__name = course

    def set_course_credit(self,credit):
        if 0<credit<=20:
            self.__credit = credit
        else:
            return f'学分不在0-20区间中'
# 获取课程名称与学分
    def get_course_name(self):
        return self.__name

    def get_course_credit(self):
        return  self.__credit
    def show_course(self):
        return f'课程名称 {self.__name},课程学分 {self.__credit}'
# 课程管理系统
class courseManage:
    # 建立一个课程名称列表
    def __init__(self):
        self.courses_list = []
    # 添加课程
    def add_course(self,course_name):
        if course_name not in self.courses_list:
            self.courses_list.append(course_name)
            #self.courses_list.append(course_credit)
            return f'添加的课程名称为{course_name}'
        else:
            return f'{course_name}已经在管理系统中，不需要重复添加'
    # 删除课程
    def del_course(self,course):

        # if course in self.courses_list:
        #     self.courses_list.remove(course)
        #     return f'课程{course}已被删除'
        # else:
        #     return f'{course}不在课程列表中'

        for course_name in self.courses_list:
            if course == course_name:
                self.courses_list.remove(course)
                return f'课程{course}已被删除'
            else:
                return f'{course}不在课程列表中'

    # 查看课程,获得相应课程名称与学分
    def seach_course(self,course):
        for course_name in self.courses_list:
            if course_name == course:
                return course_name , course1.get_course_credit()
            else:
                return f'{course_name}不在课程列表内'
    # 查看所有课程
    def all_course(self):
        # 如果列表不为空
        # if self.courses_list:
        #     for c in self.courses_list:
        #         return f'课程名称{c.get_course_name}，对应的学分{c.get_course_credit()}'
        #
        # else:
        #     return f'当前管理系统没有课程'
        #

        for course_name in self.courses_list:
            return f'课程名称{course_name}，对应的学分{course1.get_course_credit()}'

# 创建Course类实例对象
course1 = Course()
course1.set_course_name('python')
course1.set_course_credit(2.0)
print(course1.get_course_name())
print(course1.get_course_credit())
# 创建课程管理系统实例对象
course_manage = courseManage()
a1 = course_manage.add_course(course1.get_course_name())
print(a1)
# 调用courseManage创建的实例对象调用删除课程实例方法
# a2 = course_manage.del_course('python')
# print(a2)
print(course_manage.all_course())

c1 = Course()
c1.set_course_name('python')
c1.set_course_credit(2.0)

course_manage = courseManage()
a1 = course_manage.add_course(c1)
print(a1)















