"""
实战：在线课程管理系统
开发一个简单的在线课程管理系统，用于管理员课程、学生以及学生的选课情况。
系统包括课程的添加、删除，学生的注册，以及学生对课程的选课和退课功能。

创建 Course 类：
- 实例属性：课程名称、课程编号、课程容量（最大选课人数）、已选人数。 - 实例方法：展示课程信息。
- 静态方法：验证课程编号是否合法（必须是以 "C" 开头的 5 位字母和数字组合）。

创建 Student 类：
- 实例属性：学生姓名、学号、已选课程（列表）。 - 实例方法：展示学生信息。 - 静态方法：验证学号是否合法（必须为 8 位数字）。
"""
class Course:
    def __init__(self,name,seq,volume):
        self.name = name
        self.seq = seq
        self.volume = volume
        self.selected = 0
    # 显示课程信息
    def show_course(self):
        print(f'课程名称：{self.name}')
        print(f'课程编号: {self.seq}')
        print(f'课程容量: {self.volume}')
        print(f'课程已选人数: {self.selected}')
    # 使用静态方法验证课程编号是否合法 调用Course类的一个实例对象
    @staticmethod
    def verify_seq(course):
        if course.seq.isalnum() == True and len(course.seq) == 5:

            if course.seq.startswith('C',0,4) == True:
                print(f'课程编号{course.seq}合法')
            else:
                print(f'课程编号{course.seq}不合法，首字母应为‘C’')
        else:
            print(f'课程编号不合法,必须是以 "C" 开头的 5 位字母和数字组合')
class Student:
    def __init__(self,stu_name,stu_seq):   # 实例属性学生姓名、学号、已选课程列表
        self.stu_name = stu_name
        self.stu_seq = stu_seq
        self.selected_stu= []

    # 实例方法，展示学生信息
    def show_student(self):
        #course_list = []
        # if self.selected_stu:
        #     for c in self.selected_stu:
        #         course_list.append(c.name)
        # else:
        #     course_list.append(f"学生{self.stu_name}没有选课数量为0")
        # print(f'学生{self.stu_name}的学号为{self.stu_seq},已选课列表为{course_list}')
        course_list = [c.name for c in self.selected_stu] or [f"学生{self.stu_name}没有选课数量为0"]
        print(f'学生{self.stu_name}的学号为{self.stu_seq},已选课列表为{course_list}')

    # 静态方法：验证学号是否合法（必须为 8 位数字）
    @ staticmethod
    def verify_stu_seq(student):
        if student.stu_seq.isdigit() == True and len(student.stu_seq) == 8:
            print(f'学号{student.stu_seq}合法')
        else:
            print(f'学号{student.stu_seq}不合法')
'''
    创建 CourseManager 类：
 - 添加课程、删除课程、查看所有课程。
 - 添加学生、删除学生、查看所有学生。
 - 学生选课（选课时需要判断课程容量是否已满）。
 - 学生退课。使用异常处理，确保课程编号、学生学号的有效性，以及选课或退课的边界条件。
'''

class CourseManager:
    def __init__(self):
        self.courses = []
        self.students = []

    # 添加课程，创建课程列表,调用课程实例对象
    def add_course(self,course):
        if course in self.courses:
            print(f'序号为{course.seq}的{course.name}课程已经在课程列表')
        else:
            self.courses.append(course)
            print(f'序号为{course.seq}的{course.name}课程已添加在课程列表')
# 删除课程，传入字符串参数
    def del_course(self,course_id):
        for c in self.courses:
            if course_id == c.seq:
                self.courses.remove(c)
                print(f'序号为{c.seq}的{c.name}已删除')
            else:
                print(f'课程{c.seq}在课程列表中不存在')
    # 查看所有课程
    def show_all_course(self):
        for course in self.courses:

            print(course.show_course)
    # 学生姓名、学号、已选课程（列表）
    # 添加学生，创建学生列表,调用学生类的实例对象
    def add_student(self,student):
        if student in self.students:
            print(f'学号为{student.stu_seq}的学生{student.stu_name}已经在学生列表')
        else:
            self.students.append(student)
            print(f'学号为{student.stu_seq}的学生{student.stu_name}已添加在学生列表')
    # 删除学生 传入学生序号字符串参数
    def del_student(self, student_seq):
        for s in self.students:
            if student_seq == s.stu_seq:
                self.courses.remove(s)
                print(f'学号为{student_seq}的学生{s.stu_name}已删除')
            else:
                print(f'学号为{student_seq}的学生在学生列表中不存在')

    # 查看所有学生

    def show_all_student(self):
        for student in self.students:
            print(student.show_student())


     # 学生选课（选课时需要判断课程容量是否已满）,
    # 传入Student实例对象和Course实例对象参数
    def select_course(self,student,course):

         # 查看学生是否存在
        # 判断课程是否存在
         # 查看课程是否选满
        #for c in self.students:
        if student in self.students:
            if course in self.courses:
                if course.volume == course.selected:
                    print(f'序号为{course.seq}的{course.name}课程容量已满，请选其他课程')
                else:
                    student.selected_stu.append(course)
                    course.selected += 1
                    print(f'学号为{student.stu_seq}的学生{student.stu_name}已选序号为{course.seq}的{course.name}课程')
            else:
                print('该课程不存在')
        else:
            print('该学生不存在')




# 学生退课。使用异常处理，确保课程编号、学生学号的有效性，以及选课或退课的边界条件

    # 传入一个Course类实例对象，判断
    def drop_course(self,student,course):
        # 查看学生是否存在
        # 判断课程是否存在
        # 查看学生是否选过此课程
        # for c in self.students:
        if student in self.students:
            if course in self.courses:
                if course in student.selected_stu:
                    student.selected_stu.remove(course)
                    course.selected -= 1
                    print(f'学号为{student.stu_seq}的学生{student.stu_name}已将序号为{course.seq}的{course.name}课程退课')
                else:
                    print(f'学号为{student.stu_seq}的学生{student.stu_name}还未选序号为{course.seq}的{course.name}课程')
            else:
                print('该课程不存在')
        else:
            print('该学生不存在')
    #         self.courses = []
    #         self.students = []
    def display_course(self):
        for c in self.courses:
            c.show_course()
    def display_student(self):
        for s in self.students:
            s.show_student()



# 获取选课系统实例
manager = CourseManager()

# 添加课程
course1 = Course("Python", "C1001", 2)
course2 = Course("机器学习", "C1002", 3)
course3 = Course("软件测试", "C1003", 1)

# 验证课程序号是否合法
Course.verify_seq(course1)
Course.verify_seq(course2)
Course.verify_seq(course3)

manager.add_course(course1)
manager.add_course(course2)
manager.add_course(course3)


# 添加学生
student1 = Student("张三", "20250001")
student2 = Student("李四", "20250002")

# 验证学生学号是否合法 使用类名或实例对象名调用类中的静态方法
Student.verify_stu_seq(student1)
Student.verify_stu_seq(student2)


manager.add_student(student1)
manager.add_student(student2)



# 学生选课

manager.select_course(student1,course1)
manager.select_course(student2,course3)


# 学生退课
manager.drop_course(student1,course1)

# 显示所有课程
print("\n所有课程信息：")
manager.display_course()

# 显示所有学生
print("\n所有学生信息：")
manager.display_student()




