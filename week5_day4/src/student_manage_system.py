"""实战：学生管理系统单元测试实战"""
import yaml


# 题目要求
# 实现一个学生管理系统 实现一个基于命令行的学生管理系统，具备以下功能：

class Student:
    def __init__(self):
        self.stu_data = []
    def data_yaml(self):
        with open('../data/student_data.yaml','w') as file:
            yaml.safe_dump(self.stu_data,file)
    def data_read(self):
        with open('../data/student_data.yaml', 'r') as file:
            return yaml.safe_load(file)

    # 1. 添加新学生信息：输入学号、姓名、年龄和性别，添加到学生列表中。
    def add(self,id,name,age,sex):
        stu = {}
        for i in self.stu_data:
            if id == i["id"]:
                return f'学生{name}信息已存在'
        stu['id'] = id
        stu['name'] = name
        stu['age'] = age
        stu['sex']  =sex
        self.stu_data.append(stu)
        self.data_yaml()
        return f'学生{name}已添加'

    # 2. 通过学号修改学生信息：根据输入的学号修改对应学生的姓名、年龄和性别。
    def update(self,id,name,age,sex):
        for i in self.stu_data:
            if id == i['id']:
                i['name'] = name
                i['age'] = age
                i['sex']  =sex
                self.data_yaml()
                return f'学生{name}信息已修改'
        self.add(id,name,age,sex)
        self.data_yaml()
        return f'学生{name}不存在，已重新添加'

    # 3. 通过学号删除学生信息：输入学号，删除对应的学生信息。
    def delete_id(self,id):
        for i in self.stu_data:
            if id == i['id']:
                self.stu_data.remove(i)
                self.data_yaml()
                return f'学生{i["name"]}信息已删除'

        return f'学生不存在'

    # 4.通过姓名删除学生信息：输入姓名，删除所有匹配姓名的学生信息。
    def delete_name(self,name):
        for i in self.stu_data:
            if name == i['name']:
                self.stu_data.remove(i)
                self.data_yaml()
                return f'学生{name}信息已删除'
        return f'学生{name}不存在'

    # 5.通过学号查询学生信息：输入学号，查询并显示对应学生的信息。
    def query_id(self,id):
        for i in self.stu_data:
            if id == i['id']:
                return f'{id}:{i["name"]} age:{i["age"]},sex:{i["sex"]}'
        return f'学生不存在'
    # 6.通过姓名查询学生信息：输入姓名，查询并显示所有匹配学生的信息。
    def query_name(self,name):
        for i in self.data_read():
            if name == i['name']:
                return f"{i['id']}:{name} age:{i['age']},sex:{i['sex']}"
        return f'学生不存在'

    # 7. 显示所有学生信息：显示当前系统中所有学生的信息。
    def stu_info(self):
        result = ""
        for stu in self.data_read():
            result += f"ID: {stu['id']}, Name: {stu['name']}, Age: {stu['age']}, Sex: {stu['sex']}\n"
        return result.strip()  # 去掉最后的换行符


    def student_management_system(self):

        while True:

            print("\n请选择操作：")
            print("1. 添加学生信息")
            print("2. 输入学号修改学生信息")
            print("3. 输入学号删除学生信息")
            print("4. 通过姓名删除学生信息")
            print("5. 通过学号查询学生信息")
            print("6. 通过姓名查询学生信息")
            print("7. 显示所有学生信息")
            print("8. 读取文件")
            print("9. 退出系统：")
            choice = input("请输入操作编号：")
            if choice == "1":
                self.add('01','Tom',18,'male')
            elif choice == "2":
                self.update('01','Tom',20,'male')
            elif choice == "3":
                self.delete_id('01')
            elif choice == "4":
                self.delete_name('Tom')
            elif choice == "5":
                print(self.query_id('01'))
            elif choice == "6":
                self.query_name('Tom')
            elif choice == "7":
                print(self.stu_info())
            elif choice == "8":
                print(self.data_read())
            elif choice == "9":
                print("退出系统，再见！")
                break
            else:
                print("无效输入，请重新选择！")


# 主程序入口
if __name__ == "__main__":
    student = Student()
    student.student_management_system()



















