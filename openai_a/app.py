import os
from flask import Flask, request, redirect, url_for, render_template
import openai


os.environ["OPENAI_API_KEY"] = "02cd8437a7b3eedaa7c16f3605b655a9"  # 替换为你的 OpenAI API 密钥
os.environ["OPENAI_BASE_URL"] = "https://apitoken.ceba.ceshiren.com/openai/v1/"
os.environ["OPENAI_API_BASE"] = "https://apitoken.ceba.ceshiren.com/openai/v1/"
app = Flask(__name__)
messages = []

@app.route("/", methods=("GET", "POST"))
def index():
    global messages

    if request.method == "POST":
        user_msg = request.form["msg"]

        if not messages:
            messages.append({
                "role": "system",
                "content": "你是一名软件测试的面试官，你在阿里巴巴，你要为公司招聘软件测试工程师，您要面试应聘者，一次只回答一个问题"
            })

        messages.append({
            "role": "user",
            "content": user_msg
        })

        response = openai.chat.completions.create(
            model="gpt-4o-mini",  # 替换为你的模型名称
            messages=messages,
            temperature=0
        )
        answer = response.choices[0].message.content
        messages.append({
            "role": "assistant",
            "content": answer
        })

        print(f"messages: {messages}")
        print(f"answer: {answer}")

        return redirect(url_for("index", result=answer))

    result = request.args.get("result")
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True,port=5054)
