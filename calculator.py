from flask import Flask
from flask import render_template
import json

app = Flask(__name__)
# TODO: Going to have to figure out how to handle multiple users if you're using a global variable

@app.route("/hello")
def output():
    with open('hello_output.txt', 'w') as file:
        file.write('Hello')
	return "Hello World!"

matrix = []

@app.route('/rref', methods = ['POST'])
def rowReduce():
    matrix = request.get_json()
    with open('rref_output.txt', 'w') as file:
        file.write("hello????")

if __name__ == "__main__":
	app.run()
