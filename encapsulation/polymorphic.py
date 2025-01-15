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

print(isinstance(littleDoctor, Father))
print(isinstance(littleDoctor, Son))
print(isinstance(littleDoctor, AnimalDoctor))
# bool值 为True 前面对象是后面类的实例 属于子类的对象也是属于父类的对象










