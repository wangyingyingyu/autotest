"""
课堂练习：多人分组评分系统
假设有 3 名评委需要给 5 名参赛选手打分（分数范围为 1 到 10）。
使用 for 循环依次处理每个评委对选手的评分。
使用 while 循环管理整个评分流程，直到所有选手都打分完成。
最终，计算每位选手的平均分并显示结果
"""
n = 1
while n < 6:
    grade = []
    for i in range(1, 4):
        grade.append(float(input(f'第{i}名评委给第{n}名选手打分为：')))
    print(grade)
    s = sum(grade)
    average = s/len(grade)
    print(f'第{n}位选手的平均分为{average}')
    n +=1




