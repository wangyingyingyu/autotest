# 编写一个算法，实现从一个字符串中找出最长的不重复的字符串

def longest_unique_substring(input_str):
    old = input_str
    l = len(input_str)
    for i in range(l):
        strings = list(input_str).pop(i)
        for j in strings:
            if input_str[i] == j:
                strings.remove(j)

                # 示例
input_str = "asdddfaceddfdf"
#result = longest_unique_substring(input_str)
#print(result)  # 输出：faced

d = set(input_str)
print(d)
