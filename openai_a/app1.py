import os
from flask import Flask, request, redirect, url_for, render_template
import openai

class ChatApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.messages = []
        self.setup_openai()
        self.setup_routes()

    def setup_openai(self):
        os.environ["OPENAI_API_KEY"] = "02cd8437a7b3eedaa7c16f3605b655a9"
        os.environ["OPENAI_BASE_URL"] = "https://apitoken.ceba.ceshiren.com/openai/v1/"
        os.environ["OPENAI_API_BASE"] = "https://apitoken.ceba.ceshiren.com/openai/v1/"
        openai.api_key = os.getenv("OPENAI_API_KEY")
        openai.api_base = os.getenv("OPENAI_API_BASE")

    def setup_routes(self):
        @self.app.route("/", methods=("GET", "POST"))
        def index():
            if request.method == "POST":
                user_msg = request.form["msg"]

                if not self.messages:
                    self.messages.append({
                        "role": "system",
                        "content": "你是一名软件测试的面试官，你在阿里巴巴，你要为公司招聘软件测试工程师，您要面试应聘者，一次只回答一个问题"
                    })

                self.messages.append({
                    "role": "user",
                    "content": user_msg
                })

                response = openai.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=self.messages,
                    temperature=0
                )
                answer = response.choices[0].message.content
                self.messages.append({
                    "role": "assistant",
                    "content": answer
                })

                print(f"messages: {self.messages}")
                print(f"answer: {answer}")

                return redirect(url_for("index", result=answer))

            result = request.args.get("result")
            return render_template("index.html", result=result)

    def run(self, debug=True, port=5054):
        self.app.run(debug=debug, port=port)

if __name__ == "__main__":
    chat_app = ChatApp()
    chat_app.run(debug=True,port=5053)