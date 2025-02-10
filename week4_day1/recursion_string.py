"""
课堂练习：字符串反转
使用递归函数反转一个字符串，例如将 "hello" 变为 "olleh"。
"""
def reverse_string(s):

    if len(s) <= 1:
        return s

    else:
        return s[-1] + reverse_string(s[:-1])
#s[:-1] 中的 -1 表示倒数第一个字符 s[:-1] 表示从字符串的开头到倒数第二个字符（不包括最后一个字符）的子字符串。

s = "hello"
result = reverse_string(s)
print(result)

