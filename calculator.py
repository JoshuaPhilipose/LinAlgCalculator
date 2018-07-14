from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit
import brain
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# TODO: Have each method be self contained, calling only the other methods it needs.

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('calculate')
def calculate(json):
    clientID = json["clientID"] # String
    function = json["func"] # String
    rows = int(json["rows"]) # Convert both rows and cols to strings
    cols = int(json["cols"])
    values = json["values"].split(",") # NOTE: The values are now individual strings stored in a list.
    matrix = matrixify(rows, cols, values) # Stores the values in scipy/numpy matrix form as ints

    result = reroute(function, matrix) # result is in dict form
    finalResult = makeItPretty(result) # finalResult is in string/html form

    # Emit HTML to be displayed
    emit('result', finalResult)

    # with open('calculate_input.txt', 'w') as file:
    #     file.write(str(json) + '\n' + clientID + '\n' + str(matrix))

@socketio.on('my event')
def initial_connection(message):
    with open('calculate_input.txt', 'w') as file:
        file.write('Connected!')
    emit('my response', 'Connected to server.')


def matrixify(rows, cols, values):
    matrix = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(int(values.pop(0))) #pops value at index 0
        matrix.append(row)
    return matrix

def reroute(function, matrix):
    if (function == "LU Factorization"):
        return brain.LUfactorization(matrix)
    else:
        return "Sorry, this functionality is currently unavailable. Function attempted: " + function

def makeItPretty(result):
    # You're beautiful just the way you are! Except in string form
    return str(result)

if __name__ == '__main__':
    socketio.run(app)
