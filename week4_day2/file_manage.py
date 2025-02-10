# 读取 YAML 文件, 以前面复杂结果数据为例
import yaml
with open('data.yaml', 'r') as file:
    data = yaml.safe_load(file)

# 处理读取到的数据
print(data)
data['banana'] = 7

print(data)
print(type(data))