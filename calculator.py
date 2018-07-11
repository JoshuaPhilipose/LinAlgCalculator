from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit
import scipy
import scipy.linalg
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# TODO: Have each method be self contained, calling only the other methods it needs.

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('calculate')#, namespace='/cortex')
def calculate(json):
    clientID = json["clientID"]
    function = json["func"]
    rows = json["rows"]
    cols = json["cols"]
    values = json["values"].split(",") # NOTE: The values are now individual strings stored in a list.
    matrix = matrixify(rows, cols, values)

    with open('calculate_input.txt', 'w') as file:
        file.write(str(json) + '\n' + clientID + '\n' + str(matrix))
    emit('result', 'We\'re in business!')

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

if __name__ == '__main__':
    socketio.run(app)
