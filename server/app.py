#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return f"{parameter}"

@app.route('/count/<int:parameter>')
def count(parameter):
    result = ''
    for x in range(parameter):
        result += f'{x}\n'
    return result

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, num2, operation):
    if operation == '+':
        return f'{num1 + num2}'
    elif operation == '-':
        return f"{num1 - num2}"
    elif operation == '*':
        return f"{num1 * num2}"
    elif operation == 'div':
        if num2 == 0:
            return "Division by zero error! "
        else:
            return f"{num1 / num2}"
    elif operation == '%':
        return f'{num1 % num2}'


if __name__ == '__main__':
    app.run(port=5555, debug=True)
