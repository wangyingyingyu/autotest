"""
课后作业
面向对象跑步减肥
小明和小美都爱跑步
小明体重 75 公斤
小美体重 45 公斤
每次跑步会减肥 0.5 公斤
每次吃东西体重增加 1 公斤
请根据打印出跑完步之后的体重
"""
class Sport:
    def __init__(self,name,weight):
        self.name = name
        self.weight= weight
        print(f'{self.name}初始体重是{self.weight}公斤')
    # def __str__(self):
    #     print(f'{self.name}初始体重是{self.weight}公斤')

    # 跑步的次数
    count = 0
    def run(self):
        self.weight -= 0.5
        Sport.count +=1
    # 吃饭的次数
    c =0
    def eat(self):
        self.weight += 1
        Sport.c += 1

    def show(self):
        print(f'{self.name}跑步{Sport.count}次，吃了{Sport.c}次饭，体重为{self.weight}公斤')



Tom = Sport('Tom',75)

Tom.run()
Tom.run()
Tom.eat()
Tom.show()













