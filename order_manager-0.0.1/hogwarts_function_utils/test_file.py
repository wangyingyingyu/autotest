import json
from pathlib import Path

import pytest


def test_file():
    file = open('sort.py')
    r = file.read()
    print(r)

    file2 = open('demo.txt', mode='w')
    file2.write('123\n456')
    file2.close()

    with open('demo2.txt', 'a+') as file:
        file.write('123')

    r = Path('demo.txt').read_text(encoding='U8')

    Path('demo2.txt').write_text('123')

    bytes1 = '中国'.encode('U8')
    bytes2 = '中国'.encode('GBK')
    print(bytes1)
    print(bytes2)

    Path('demo3.txt').write_bytes(bytes1 + bytes2)


def concat(path1, path2, path3):
    """
    合并file1 file2 写入到file3
    :param file1:
    :param file2:
    :return:
    """

    file_1 = open(path1)
    content_1 = file_1.read()
    file_1.close()

    file_2 = open(path2)
    content_2 = file_2.read()
    file_2.close()

    content = content_1 + content_2

    file3 = open(path3, 'w')
    file3.write(content)
    file3.close()

    # with open(path1) as file:
    #     content_1 = file.read()
    #
    content_1 = Path(path1).read_text()


def test_concat():
    # todo: 编写测试用例

    file1 = open('1.txt', 'w')
    file1.write('123')
    file1.close()

    file2 = open('2.txt', 'w')
    file2.write('4564')
    file2.close()

    concat('1.txt', '2.txt', '3.txt')
    content = open('3.txt').read()
    assert content == '123456'


@pytest.mark.parametrize(
    'passwd',
    [
        '123456',
        'abcdefdfs',
        'as52345fasdf4'
    ]
)
def test_passwd_length(passwd):
    assert len(passwd) >= 8


def test_json():
    data = {}
    data['name'] = '123'
    data['id'] = 1
    data['status'] = True
    print()
    r = json.dumps(data, indent=2)
    print(r)

    data = json.loads('{"name": "seven"}')
    print(data)
    print(data['name'])
