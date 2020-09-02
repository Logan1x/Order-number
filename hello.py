import os
from flask import Flask, render_template,request
import random

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def hello1():
    len = request.form['len']
    print(len)
    return render_template("index.html", len =len)

@app.route('/op')
def hello2():
    len = request.form['len']
    print(len)
    return render_template("output.html", len =len)


# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404.html'), 404

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug="True")

