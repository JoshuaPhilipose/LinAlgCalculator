from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit
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
    with open('calculate_input.txt', 'w') as file:
        file.write(str(json) + '\n')
    emit('result', 'We\'re in business!')

@socketio.on('my event')
def initial_connection(message):
    with open('calculate_input.txt', 'w') as file:
        file.write('Connected!')
    emit('my response', 'Connected to server.')

if __name__ == '__main__':
    socketio.run(app)
