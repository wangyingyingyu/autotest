"""YAML 文件操作
将相同的配置转换为 YAML 格式保存到 test_config.yaml 文件。
从文件中加载 YAML 配置并打印。
1. **标签（Key）和内容（Value）之间用冒号（:）来分隔**，而冒号后面应该有一个空格。
2. **保持正确的缩进**。YAML 使用空格进行缩进，不能使用制表符（Tab）。
3. **确保文件的编码为 UTF-8**，特别是当文件中包含中文字符时。你可以使用文本编辑器（如 VSCode、Notepad++ 等）来检查文件的编码格式。

### 检查格式的步骤：
- 使用支持 YAML 语法高亮的文本编辑器来查看文件。
- 确保键值对的格式为 `key: value`，并且有适当的空格。
- 如果需要嵌套结构，使用两个空格或四个空格进行缩进。
"""

import yaml
data = {
    "app_name": "TestApp",
    "version": "0.1",
    "libraries": ["numpy", "pandas"]
}
with open('test_config.yaml','w') as file:
    yaml.safe_dump(data,file)
with open("test_config.yaml",'r') as f:
    datas = yaml.safe_load(f)
print(datas)
print(type(datas))
print(datas["version"])
"""`.yaml` 文件中，存在重复的键（`name` 和 `count`），这会导致 YAML 的解析错误，进而导致语法高亮显示不正常。
yaml
name: apple
count: 9
name: orange  # 重复的键
count: 8     # 这将覆盖上面的 count
1. **确保键的唯一性**: 将每一组相关的键放在一个对象（或映射）中。
yaml
fruits:
  - name: apple
    count: 9
  - name: orange
    count: 8
"""