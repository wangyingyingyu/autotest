"""
实战：英雄游戏
设计一个游戏，可以定义各种英雄，并实现英雄间的打斗，最终得到打斗的结果。
要求
定义一个英雄类：
- 此英雄类需要包含 姓名、 血量、 攻击力、 还需要有一个方法为讲台词。
- 根据英雄类，实例化不同的英雄对象：每个英雄需要在实例化的时候，就有自己的姓名、攻击力、血量。
- 每个英雄的血量不可以直接被获取或者修改。

定义法师类英雄
- 法师类：


  1. 法师类继承于 Hero 类。
  2. 法师类多了魔力的属性
  3. 法师类多了一个放技能的方法。
"""

class Hero:
    def __init__(self,name,blood,attack):
        self.name = name
        self.__blood = blood
        self.attack = attack
    # 获取血量
    def blood(self,blood):
        print(f'血量为{blood}')

    def speak(self):
        print(f'欢迎来到英雄联盟，我的名字为{self.name}')

class Master(Hero):
    def __init__(self,name,blood,attack,magic):
        super().__init__(name,blood,attack)
        self.magic = magic

    def speak(self):
        super().speak()
        print('你好')



    def technique(self):
        print('放技能')
        if self.magic < 50:
            print("蓝量不足")
        else:
            print("施展魔力技能")
            self.magic -= 50
    def show(self):
        print(f'{self.name}的攻击力为{self.attack}',end=',')


# 实例化Hero对象
hero1 = Hero('英雄1',60,90)

master = Master('法师',80,70,100)

master.speak()
master.technique()
master.show()
master.blood('80')


























