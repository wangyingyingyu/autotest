# 编写一个 Python 程序，输出所有由数字 1、2、3、4 组成的互不相同且无重复数字的三位数。
# 即个位，十位，百位互不相同且无重复数字
def numic():
    l = []
    for i in range(1,5):
        for j in range(1,5):
                for k in range(1,5):
                    l.append(str(i*100+j*10+k))
    return l


new_l  =numic()
print(new_l)
print(type(new_l[1]))
new_num = []
for num in new_l:

    if int(num[0]) != int(num[1]) and int(num[0]) != int(num[2]) and int(num[2]) != int(num[1]):

        new_num.append(num)

print(new_num)




