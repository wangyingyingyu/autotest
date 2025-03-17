from flask import Flask, render_template

app3 = Flask(__name__)

@app3.route("/html", methods=["GET"])
def html_demo():
    return render_template('demo.html')

if __name__ == '__main__':
    app3.run(debug=True, port=5052)  # 确保端口为 5052