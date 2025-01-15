import random


class Hero:
    red_team = []
    blue_team = []

    def __init__(self, name, hp, power, speed, team, auto=True):
        self.name = name
        self.hp = hp
        self.power = power
        self.speed = speed  # 速度可取范围[1,5],可以为小数
        self.team = team
        self.auto = auto
        if self.team == 'red':
            Hero.red_team.append(self)
        else:
            Hero.blue_team.append(self)

    def __str__(self):
        return f'{self.name}(hp:{self.hp:.1f}/power:{self.power:.1f}/speed:{self.speed:.1f})'

    def say_words(self):
        pass

    def move(self):
        if self.hp > 0:
            if self.auto:
                self.auto_attack()
            else:
                self.manual_attack()
            # print('-----')
        # else:
        # print(f'{self.name}已死亡')

    def attack(self, target):
        """
        普通攻击，造成自身能力值的伤害
        :param target:
        :return:
        """
        print(f'{self.name}向{target.name}({target.hp})发起了攻击')
        target.injured(self.power)

    def injured(self, damage):
        self.hp -= damage
        if self.hp > 0:
            print(f'{self.name}受到了{damage}点伤害，hp:{self.hp:.1f}')
        else:
            if self in self.get_team():
                print(f'{self.name}({self.hp:.1f})似啦！！！丸辣！')
                self.get_team().remove(self)

    def heal(self, recovery):
        self.hp += recovery
        print(f"{self.name}回复了{recovery}点血量，hp:{self.hp:.1f}")

    def speed_up(self, extra=1):
        self.speed = min(5, self.speed + extra)
        print(f'{self.name}的速度提高了，speed:{self.speed}')

    def get_enemy(self):
        if self.team == 'red':
            return Hero.blue_team
        else:
            return Hero.red_team

    def get_team(self):
        if self.team == 'red':
            return Hero.red_team
        else:
            return Hero.blue_team

    def auto_attack(self):
        if isinstance(self, Assist):
            if self.get_team():
                target = random.choice(self.get_team())
                self.attack(target)
        else:
            if self.get_enemy():
                target = random.choice(self.get_enemy())
                self.attack(target)

    def manual_attack(self):
        pass


class Mage(Hero):
    """
    法师
    fire_ball：消耗蓝量，对目标造成1.5倍能力值的伤害。蓝量不足时，只能使用普通攻击
    亡语：死亡后对所有剩余敌人造成伤害，敌人均摊总和为（2*能力值+2*mp）的伤害
    """

    def __init__(self, name, hp=90, power=20, speed=2, team='red', mp=100):
        super().__init__(name, hp, power, speed, team)
        self.mp = mp

    def say_words(self):
        print(f'{self.name}:元素的低语，是命运的指引；在火焰与寒冰的交织中，我掌控一切！')

    def attack(self, target):
        if self.mp >= 30:
            self.mp -= 30
            self.fire_ball(target)
        else:
            print(f'{self.name}魔法不足,只能使用普通攻击')
            Hero.attack(self, target)

    def injured(self, damage):
        self.hp -= damage
        if self.hp > 0:
            self.hp -= damage
            print(f'{self.name}受到了{damage}点伤害，hp:{self.hp:.1f}')
        else:
            if self in self.get_team():
                print(f'{self.name}({self.hp:.1f})受到了{damage}点伤害，濒临死亡')
                self.death_rattle(self.get_enemy())
                self.get_team().remove(self)

    def fire_ball(self, target):
        """
        火球术，消耗30点蓝量，造成1.5倍攻击力伤害
        :param target:
        :return:
        """
        print('“微火起点，足以化作烈焰。”')
        print(f'{self.name}向{target.name}({target.hp:.1f})释放了火球，mp:{self.mp}')
        target.injured(self.power * 1.5)

    def death_rattle(self, enemy):
        """
        所有敌人均摊受到自身攻击力3倍的伤害
        :param enemy: 敌人列表
        """
        print('呵...知识的火焰...终将燃尽...但真理...永不熄灭...烈焰焚天！')
        aoe_damage = (self.power * 2 + self.mp * 2) / len(enemy)
        for i in enemy:
            i.injured(aoe_damage)


class Shield(Hero):
    """
    盾兵，额外拥有护盾值，受到攻击时优先消耗护盾值
    shield_slam：使用护盾猛击对手，造成0.75倍攻击力的伤害，并获得当前血量20%的护盾(无上限）
    """

    def __init__(self, name, hp=80, power=20, speed=1, team='red', armor=70):
        super().__init__(name, hp, power, speed, team)
        self.armor = armor

    def say_words(self):
        print(f'{self.name}:钢铁为盾，怒火为刃！今日的战场，只能留下胜者的咆哮！')

    def attack(self, target):
        self.shield_slam(target)

    def injured(self, damage):
        if damage <= self.armor:
            self.armor -= damage
            print(f'{self.name}消耗了{damage}点护盾，armor:{self.armor}')
        elif self.armor < damage < self.hp + self.armor:
            damage = damage - self.armor
            self.armor = 0
            self.hp -= damage
            print(f'{self.name}受到了{damage}点伤害，护盾被消耗了，hp:{self.hp:.1f}')# `:.1f` 表示将数字格式化为小数点后1位的浮点数
        else:
            self.hp -= damage
            self.armor = 0
            print(f'{self.name}({self.hp:.1f})似啦！！！丸辣！')
            self.get_team().remove(self)

    def shield_slam(self, target):
        """
        护盾猛击，造成0.75倍攻击力的伤害，并恢复当前血量20%的护盾（无上限）
        :param target:攻击目标
        """
        print(f'{self.name}向{target.name}({target.hp})释放了护盾猛击，护盾值回复了，hp:{self.hp:.1f}/armor:{self.armor}')
        target.injured(self.power * 0.75)
        self.armor += self.hp / 20


class Assist(Hero):
    """
    辅助
    support：只能以友军为目标。消耗蓝量，产生随机效果：回复友军生命值或提高友军速度
    """

    def __init__(self, name, hp=80, power=20, speed=2, team='red', mp=100):
        super().__init__(name, hp, power, speed, team)
        self.mp = mp

    def say_words(self):
        print(f'{self.name}:光明庇佑同伴，生命源泉涌动；在我的守护下，你们无需畏惧黑暗')

    def attack(self, target):
        if self.mp >= 40:
            print('战意如风，守护如山；去吧，我的力量与你同在')
            if random.randint(0, 1):
                self.mp -= 40
                print(f'{self.name}治愈了{target.name}({target.hp})，mp:{self.mp}')
                target.heal(self.power / 2)

            else:
                self.mp -= 40
                print(f'{self.name}加速了{target.name}({target.hp})，mp:{self.mp}')
                target.speed_up(extra=0.7)

        else:
            self.mp += 60
            print('魔法不足,本回合回复法力值')


class Ninja(Hero):
    """
    忍者
    被动技能：有概率闪避攻击，速度越快，闪避几率越高
    每次闪避成功提升自身能力值，每次攻击提高自身速度

    """

    def __init__(self, name, hp=100, power=20, speed=2, team='red'):
        super().__init__(name, hp, power, speed, team)

    def say_words(self):
        print(f'{self.name}:影随身隐，刀至命绝；你只会察觉到最后一丝风声')

    def injured(self, damage):
        if random.randint(0, 6 - int(self.speed)):
            self.hp -= damage
            if self.hp > 0:
                self.hp -= damage
                self.speed = max(5, self.speed + 1)
                print(f'{self.name}受到了{damage}点伤害，速度提升了，hp:{self.hp:.1f}')
            else:
                print(f'{self.name}({self.hp:.1f})似啦！！！丸辣！')
                self.get_team().remove(self)
        else:
            print(f'{self.name}闪避了攻击，自身能力值提高了')
            self.power *= 1.2


class Swardsman(Hero):
    """
    剑客
    draw：每次攻击造成1.1倍能力值的伤害并叠加剑意，每层剑意为自身提供1单位速度，两层剑意时，下次攻击清空剑意并释放二连击，造成两次1.2倍能力值的伤害，
    """

    def __init__(self, name, hp=100, power=20, speed=2, team='red'):
        super().__init__(name, hp, power, speed, team)
        self.sword_intent = 0

    def say_words(self):
        print(f'{self.name}:剑随心走，影随风动。你，还不配让我用出全力')

    def attack(self, target):
        self.draw(target)

    def draw(self, target):
        """
        主要技能
        :param target: 攻击目标
        """
        if self.sword_intent < 2:
            print(f'{self.name}:剑鸣破空，一瞬即永恒！剑指{target.name}({target.hp})!')
            self.sword_intent += 1
            target.injured(self.power * 1.1)
        else:
            print(f'{self.name}:剑心无尘，万物皆为刃；这一击，你看得清吗？剑指{target.name}({target.hp})!')
            target.injured(self.power * 1.2 * 2)
            # target.injured(self.power * 1.2)
            self.sword_intent = 0
        self.speed += self.sword_intent + 1


class Arena:
    def __init__(self, team_size):
        print("""'1': Mage,\n'2': Shield,\n'3': Assist,\n'4': Ninja,\n'5': Swardsman""")
        for i in range(2):
            if i == 0:
                team = 'red'
                print('-' * 10 + '红队选择英雄' + '-' * 10)
            else:
                team = 'blue'
                print('-' * 10 + '蓝队选择英雄' + '-' * 10)
            for j in range(team_size):
                choice = input('请选择英雄:')
                self.hero_selector(choice, name=team + choice, team=team)

        print('红队阵容', end=':')
        for i in Hero.red_team:
            print(i, end='  ')
        print()
        print('蓝队阵容', end=':')
        for i in Hero.blue_team:
            print(i, end='  ')
        print()

        self.hero_list = Hero.red_team.copy()
        self.hero_list.extend(Hero.blue_team)
        # print('英雄选择完毕', self.hero_list)

    @staticmethod
    def hero_selector(choice, name, team):
        heroes = {
            '1': Mage,
            '2': Shield,
            '3': Assist,
            '4': Ninja,
            '5': Swardsman
        }
        if choice in heroes:
            hero = heroes[choice](name=name, team=team)
            # print(hero.red_team)
            # print(hero.blue_team)
            return hero
        else:
            print(choice, '??')

    def war(self):
        round_num = 1
        # print(self.hero_list)
        # 轮流说台词
        for hero in self.hero_list:
            hero.say_words()
        # 轮流行动
        while True:
            # 每次行动前按速度排序
            speed_order = sorted(self.hero_list, key=lambda x: x.speed, reverse=True)
            # 速度高的先行动
            for hero in speed_order:
                hero.move()  # 英雄行动
            print('-' * 10, round_num, '-' * 10)

            if round_num % 3 == 0:  # 每3个回合打印一次阵容
                print('红队阵容', end=':')
                for i in Hero.red_team:
                    print(i, end='  ')
                print()
                print('蓝队阵容', end=':')
                for i in Hero.blue_team:
                    print(i, end='  ')
                print()

            # 判断赢家
            if not Hero.red_team and not Hero.blue_team:
                print('无人幸免，战斗结束')
                return round_num
            elif not Hero.red_team or not Hero.blue_team:
                if Hero.red_team:
                    print('红队获胜')
                    return round_num
                else:
                    print('蓝队获胜')
                    return round_num

            round_num += 1
            # 回合数超过50时，强制结束
            if round_num >= 50:
                return 50


if __name__ == '__main__':
    arena = Arena(2)
    arena.war()
