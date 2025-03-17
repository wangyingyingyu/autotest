import random
import string

def generate_num(length=6):

    characters = string.ascii_letters + string.digits  # 包含字母和数字

    num = ''.join(random.choice(characters) for _ in range(length))
    return num


if __name__ == "__main__":
    print("默认长度验证码:", generate_num())
    print("自定义长度验证码:", generate_num(8))





