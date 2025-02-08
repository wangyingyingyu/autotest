"""
print("|" + "  hogworts  " + "|")
print("|" + "  hogworts  ".strip() + "|")
print("|" + "  hogworts".strip() + "|")
print("|" + "hogworts  ".strip() + "|")
print("|" + "  h o g w o r t s  ".strip() + "|")
print("|" + "bachogwortsabc".strip("cba") + "|")



print("a-b-c-d".split("-"))
print("a-b-c-d".split("-", 2))
print("a--b-c-d".split("-"))
print("a-+b-c-d".split("-+"))
print("a b\tc\nd\re".split())
print("a b c d e".split(" ", 3))
print("a b\tc\nd\re")


stu = {'name': 'Tom', 'age': 23, 'gender': 'male', 'address': 'BeiJing'}

stu.setdefault("hobby1")
print(stu)
stu.setdefault("hobby2", "无")
print(stu)

print("".join(("a","b","c")))
print("-".join(("a","b","c")))
print("->".join(("a","b","c")))
print("->".join(["a","b","c"]))
print("->".join({"a","b","c"}))
print("->".join({"a":"A","b":"B","c":"C"}))

# 定义可变关键字参数
def print_info(**kwargs):
    print(kwargs)

    print(type(kwargs))
    for k,v in kwargs.items():
        print(k, v)
    print("*" * 10)

print_info(Tom=18, Jim=20, Lily=12)
print_info(name="tom",age=22,gender="male",address="BeiJing")

# 不确定个数数字求和
def my_sum(*args):
    print(args)
    print(*args)
    print(type(args))
    s = 0
    for i in args:
        s += i

    print(s)
    print("*" * 10)

my_sum(1,2,3)
my_sum(1,2,3,4)
my_sum(1,2,3,4,5)
my_sum(1,2,3,4,5,6)
"""
# 中医
class Father:
    def cure(self):
        print("使用中医方法进行治疗。。。")

# 西医
class Son:
    def cure(self):
        print("使用西医方法进行治疗。。。")

# 兽医
class AnimalDoctor:
    def cure(self):
        print("使用兽医方法进行治疗。。。")

# 患者
class Patient:
    def need_doctor(self, doctor):
        doctor.cure()


if __name__ == '__main__':
    old_doctor = Father()
    little_doctor = Son()
    animal_doctor = AnimalDoctor()

    patient = Patient()

    patient.need_doctor(old_doctor)
    patient.need_doctor(little_doctor)
    patient.need_doctor(animal_doctor)





