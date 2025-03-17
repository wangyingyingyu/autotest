import json
import os

import openai

os.environ["OPENAI_API_KEY"] = "02cd8437a7b3eedaa7c16f3605b655a9"  # 将个人token替换到这个位置
os.environ["OPENAI_BASE_URL"] = "https://apitoken.ceba.ceshiren.com/openai/v1/"
os.environ["OPENAI_API_BASE"] = "https://apitoken.ceba.ceshiren.com/openai/v1/"


if __name__ == "__main__":
    messages = []
    messages.append({"role": "system",
                 "content": "你是一名软件测试的面试官，你在阿里巴巴，你要为公司招聘软件测试工程师，您要面试应聘者，一次只回答一个问题"
                 })
    for i in range(10):
        user_prompt = input()
        messages.append({
                    'role':'user',
                    'content':user_prompt
                })
        r = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )
        content = r.choices[0].message.content
        messages.append({
            'role': 'assistant',
            'content': content
        })
        raw= json.dumps(messages,indent=2,ensure_ascii=False)
        print(raw)
