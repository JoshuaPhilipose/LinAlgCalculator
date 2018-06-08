from flask import Flask, render_template, request
import json

app = Flask(__name__)
# TODO: Have each method be self contained, calling only the other methods it needs.

# @app.route("/hello")
# def output():
#     # with open('hello_output.txt', 'w') as file:
#     #     file.write('Hello')
# 	return "Hello World!"

@app.route('/rref', methods=['POST'])
def rowReduce():
    matrix = request.get_json()
    with open('rref_output.txt', 'w') as file:
        file.write(json.dumps(matrix))
    return "OK"

if __name__ == "__main__":
	app.run()
