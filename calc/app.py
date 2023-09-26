from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

operations = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
}


@app.route('/math/<operation>')
def calc(operation):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    func = operations[operation]
    return str(func(a,b))