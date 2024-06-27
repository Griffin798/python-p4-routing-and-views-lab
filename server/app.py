from flask import Flask
from werkzeug.urls import quote

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route("/print/<string:param>")
def print_string(param):
    print(param)
    return f"<p>{param}</p>"

@app.route("/count/<int:param>")
def count(param):
    output = ""
    for i in range(1, param + 1):
        output += f"{i}<br>"
    return output

@app.route("/math/<int:num1>/<string:operation>/<int:num2>")
def math(num1, operation, num2):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "div":
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero!"
    elif operation == "%":
        if num2 != 0:
            result = num1 % num2
        else:
            return "Error: Division by zero!"
    else:
        return "Error: Invalid operation!"
    
    return f"<p>The result of {num1} {operation} {num2} is {result}</p>"

if __name__ == "__main__":
    app.run(debug=True)
