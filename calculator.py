from flask import Flask, render_template, request
import json

app = Flask(__name__)
# TODO: Have each method be self contained, calling only the other methods it needs.

# @app.route("/hello")
# def output():
#     # with open('hello_output.txt', 'w') as file:
#     #     file.write('Hello')
# 	return "Hello World!"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rref', methods=['POST'])
def rowReduce():
    matrix = (request.values).to_dict()
    with open('rref_output.txt', 'w') as file:
        file.write(str(matrix) + '\n')
        file.write(str(type(matrix)) + '\n')
        file.write(str(list(matrix.keys())[0] + '\n'))
    return '{"sho" : "bhit"}'

if __name__ == "__main__":
	app.run()
