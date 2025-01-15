"""
# 常见的可变类型 列表list[] 字典{key:value, key:value} 集合{}
a = [1,2,3,4]
print(f'未修改的内存地址{id(a)}')
a.append(5)
print(f'修改的内存地址{id(a)}')

# 字典
b = {'001':{"name":'Tom',"age":18},
    '002':{"name":'Eve',"age":17}}
print(b,id(b))
b['002']["age"] = 16
print(b,id(b))
def get_number():
    num = input("请输入一个数字：")
    num = int(num)
    return num
    num=0



print(get_number())

def show():
    print("循环前输出内容")
    for i in range(10):
        print(i)
        if i == 2:
            return
    print("循环后输出内容")

print("函数调用前输出内容")
show()
print("函数调用后输出内容")
"""
def getTwoNum():
    a = int(input("请输入第一个数字："))
    b = int(input("请输入第二个数字："))
    return a, b

m, n = getTwoNum()
print(m, n)




"""
课后作业
定义一个单独的 fight 函数
在打斗之前，需要两个英雄先讲出台词。
这个 fight 函数要求实现两个英雄的多轮回合制对打功能。最后需要返回一个赢家。
创建一个测试用例文件，导入被测函数，并对它完成单元测试。
"""
class Hero:
    def __init__(self, name, hp, power):
        # 实例属性在构造函数内被初始化
        self.name = name
        self.hp = hp
        self.power = power

    # 定义方法
    def speak(self):
        print(f"欢迎来到英雄联盟，我的名字是{self.name}，我的血量为{self.hp}")

# 法师类英雄
class APCHero(Hero):

    def __init__(self, name, hp, power, mp):
        # 调用父类初始化方法去初始化父类的属性
        super().__init__(name, hp, power)
        # 魔力属性
        self.mp = mp

    def speak(self):
        super().speak()
        print("我是大美女")

    # 放技能方法
    def charm(self):
        if self.mp < 50:
            print("蓝量不足")
        else:
            print("施展魅惑技能")
            self.mp -= 50


jinx = Hero("jinx", 1000, 100)

# 实例对象.方法名 => 即可调用实例
jinx.speak()

diaochan = APCHero("貂蝉", 1200, 80, 70)
diaochan.speak()
diaochan.charm()


def fight(hero1: Hero, hero2: Hero):
    hero1.speak()
    hero2.speak()
    hero1_hp = hero1.hp
    hero2_hp = hero2.hp
    hero1_name = hero1.name
    hero2_name = hero2.name
    while True:
        hero1_hp = hero1_hp - 10
        hero2_hp = hero2_hp - 10
        # 当第一个英雄的血量小于0 或 当第二个英雄的血量小于0
        if hero1_hp <= 0 or hero2_hp <= 0:
            if hero1_hp > hero2_hp:
                # 字面量插值 - 字符串
                print(f"英雄{hero1_name}赢了")
                return hero1_name
            elif hero1_hp < hero2_hp:
                print("英雄赢了", hero2_name)
                return hero2_name
            else:
                return "平局"

def test_fight():
    jinx = Hero("jinx", 1000, 100)
    diaochan = APCHero("貂蝉", 1200, 80, 70)
    fight(jinx, diaochan)







