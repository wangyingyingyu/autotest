"""
课后作业
定义一个单独的 fight 函数
在打斗之前，需要两个英雄先讲出台词。
这个 fight 函数要求实现两个英雄的多轮回合制对打功能。最后需要返回一个赢家。
创建一个测试用例文件，导入被测函数，并对它完成单元测试
"""
class Hero:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def speak(self):
        return f"{self.name}: 让我们开始战斗！"

    def attack(self, other):
        other.health -= self.power
        return other.health

def fight(hero1, hero2):
    print(hero1.speak())
    print(hero2.speak())

    while hero1.health > 0 and hero2.health > 0:
        # Hero 1 attacks
        print(f"{hero1.name} 攻击 {hero2.name}，造成 {hero1.power} 点伤害。")
        hero1.attack(hero2)

        # 检查 hero2 是否死亡
        if hero2.health <= 0:
            return hero1.name

        # Hero 2 attacks
        print(f"{hero2.name} 攻击 {hero1.name}，造成 {hero2.power} 点伤害。")
        hero2.attack(hero1)

        # 检查 hero1 是否死亡
        if hero1.health <= 0:
            return hero2.name

    return None

# 测试用例
if __name__ == '__main__':
    hero1 = Hero("勇士", 100, 20)
    hero2 = Hero("法师", 80, 30)

    winner = fight(hero1, hero2)
    print(f"赢家是: {winner}")  # 预期勇士获胜

    hero1 = Hero("骑士", 90, 15)
    hero2 = Hero("刺客", 50, 25)

    winner = fight(hero1, hero2)
    print(f"赢家是: {winner}")  # 预期刺客获胜



