from flask import Flask, jsonify, render_template

app3 = Flask(__name__)

@app3.route("/json",methods=["POST"])
def json_demo():
    return jsonify(name="lili",age=10)


@app3.route("/html",methods=["get"])
def html_demo():
    return render_template('demo.html')


if __name__ == '__main__':
    app3.run(debug=True,port=5052)
