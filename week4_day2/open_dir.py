"""
打开文件：
使用 with open(file1, "r") as f1 打开文件，确保文件在使用后自动关闭。
"r" 表示以只读模式打开文件。

读取内容：
使用 f1.read() 和 f2.read() 读取文件内容。

写入新文件：
使用 with open('D:/bilibili-python/data.txt', "w") as file 打开目标文件，模式为 "w"（覆盖写入）。
使用 file.write(content1) 和 file.write(content2) 将内容写入文件。

读取并打印新文件内容：
使用 with open('D:/bilibili-python/data.txt', "r") as file 重新打开文件，读取并打印内容。

文件路径：
file1 和 file2 是文件路径字符串，传递给函数时不需要额外处理。

使用 with 语句可以确保文件在使用后自动关闭，避免资源泄漏。
"""

def concat(file1, file2):
    # 打开文件并读取内容
    with open(file1, "r") as f1, open(file2, "r") as f2:
        content1 = f1.read()
        content2 = f2.read()

    # 将内容写入新文件
    with open('D:/bilibili-python/data.txt', "w") as file:
        file.write(content1)
        file.write(content2)

    # 读取并打印新文件的内容
    with open('D:/bilibili-python/data.txt', "r") as file:
        content = file.read()
        print(content)

# 文件路径
file1 = "D:/bilibili-python/1.txt"
file2 = "D:/bilibili-python/2.txt"

# 调用函数
concat(file1, file2)



