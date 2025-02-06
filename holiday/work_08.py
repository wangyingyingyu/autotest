"""
John是一名打字员，他有一个习惯就是切换大小写时从来不按 SHIFT键，而是只用 Caps Lock键。
老板为了监督John的工作，想统计John每天敲了多少次键盘，让我们编写一个函数来实现这个想法吧，
>备注:输入的是字符串，只包含大小写英文字母。键盘初始默认是小写状态。
>示例:
>输入:aa，返回2，因为敲了`a,a`。
>输入:Aa，返回4，因为敲了`Cpas Lock, A, Cpas Lock,a 。
"""


def count_keypresses(s):
    keypresses = 0
    caps_lock = False  # 初始状态为小写

    for char in s:
        if char.islower():  # 当前字符是小写字母
            if caps_lock:  # 如果当前是大写状态，需要按Caps Lock
                keypresses += 1  # 按Caps Lock开关
                caps_lock = not caps_lock  # 切换状态
            keypresses += 1  # 输入小写字母

        elif char.isupper():  # 当前字符是大写字母
            if not caps_lock:  # 如果当前是小写状态，需要按Caps Lock
                keypresses += 1  # 按Caps Lock开关
                caps_lock = not caps_lock  # 切换状态
            keypresses += 1  # 输入大写字母

    return keypresses



print(count_keypresses("aa"))
print(count_keypresses("Aa"))
print(count_keypresses("aAaa"))
print(count_keypresses("AAAaa"))