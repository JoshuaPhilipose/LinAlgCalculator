from flask import Flask
import json
app = Flask(__name__)

@app.route("/hello")
def output():
	return "Hello World!"

@app.route('/rref', methods = ['POST'])
def rowReduce():
    matrix = request.get_json()
    return 777

if __name__ == "__main__":
	app.run()
