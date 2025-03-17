from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("blog.html")


if __name__ == '__main__':
    app.run(debug=True,port=5054)