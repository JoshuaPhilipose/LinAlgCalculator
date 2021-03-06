from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit
import brain
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisasupersecretkey!'
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
    # if (function == "Row Echelon Form"):
    #     return brain.ref(matrix)
    # elif (function == "Row Reduced Echelon Form"):
    #     return brain.rref(matrix)
    if (function == "Inverse"):
        return brain.inverse(matrix)
    elif (function == "LU Factorization"):
        return brain.LUfactorization(matrix)
    elif (function == "QR Factorization"):
        return brain.QRFactorization(matrix)
    elif (function == "SVD Decomposition"):
        return brain.SVDDecomposition(matrix)
    # elif (function == "Find Eigenvalues"):
    #     return brain.evalues(matrix)
    # elif (function == "Find Eigenvectors"):
    #     return brain.evectors(matrix)
    elif (function == "Orthogonal Basis"):
        return brain.obasis(matrix)
    elif (function == "Orthonormal Basis"):
        return brain.onbasis(matrix)
    elif (function == "Determinant"):
        return brain.determinant(matrix)
    elif (function == "Trace"):
        return brain.trace(matrix)
    elif (function == "Norm"):
        return brain.norm(matrix)
    elif (function == "Condition"):
        return brain.condition(matrix)
    elif (function == "Rank"):
        return brain.rank(matrix)
    elif (function == "Signed Logarithm"):
        return brain.QRFactorization(matrix)
    # elif (function == "Matrix Multiplication"):
    #     return brain.mmult(matrix)
    # elif (function == "Ax = b"):
    #     return brain.axb(matrix)
    else:
        return "<p><br>Sorry, this functionality is currently unavailable. Function attempted: " + function + ".</p> <br> This site is still under development. Thank you for being an early user - feel free to leave feedback below!"

def makeItPretty(result):
    if isinstance(result, dict):
        resultString = '<br>'
        for key in result.keys():
            resultString += '<div class="row"><h5> ' + key + ": </h6>"
            resultString += '<p>' + str(result[key]) + '</p>'
            resultString +=  '</div>'
        return resultString
    else:
        return str(result)

if __name__ == '__main__':
    socketio.run(app)
