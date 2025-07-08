import yaml


def get_data():
    with open('./data/recipients.yaml', 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    """
    `send_keys()` 只接受字符串参数，因此需要将列表格式化为字符串
    [
    ['赫敏', '15560064465', '霍格沃兹学院格兰芬多'],
    ['哈利', '15560064466', '霍格沃兹学院格兰芬多'],
    ['罗恩', '15560064467', '霍格沃兹学院格兰芬多']
]
通过 `join` 进行合并, 并用换行符连接names = "\n".join([user[0] for user in user_data])
    """
    print(data)
    datas = "\n".join([str(d) for d in data])
    print(datas)

    return datas
get_data()