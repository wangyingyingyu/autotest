# sys常用属性

# sys.argv 获取命令行参数列表，包括脚本名称和传递给脚本的参数 其结果是以列表的形式存储
import sys
script_name = sys.argv[0]
argument = sys.argv[1:]
print('脚本名称：',script_name)
print('命令行参数：', argument)

# sys.version 存储当前python解释器版本信息
print("当前解释器版本信息：", sys.version)

# sys.version_info 获取当前解释器的版本信息，以元组的形式返回详细的版本信息
print("详细的python解释器版本：",sys.version_info)

# sys.platform 获取当前操作系统平台的名称
print("当前操作系统平台名称：", sys.platform)


# sys.modules 返回已导入的模块信息，返回形式为字典
for module_name,module in sys.modules.items():
    print(f"模块名：{module_name},模块信息{module}")
