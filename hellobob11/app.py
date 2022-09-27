from flask import Flask
from flask import request

app = Flask(__name__)
app.debug = True

class Hello:
    def index(self):
        return 'Hello Bob from yoonan<br>Park_Soo_Hyun Mentor Nim Jjang Jjang'

    def add(self, x, y):
        return str(x+y)

    def sub(self, x, y):
        return str(x-y)

@app.route('/')
def index():
        return 'Hello Bob from yoonan<br>Park_Soo_Hyun Mentor Nim Jjang Jjang'

@app.route('/add')
def add():
    a = request.args.get("a", "0", int)
    b = request.args.get("b", "0", int)

    return "{}".format(a+b)

@app.route('/sub')
def sub():
    a = request.args.get("a", "0", int)
    b = request.args.get("b", "0", int)

    return "{}".format(a-b)

if __name__ == "__main__":
    h = Hello()
    app.run(host='0.0.0.0', port=8086)