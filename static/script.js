$(document).ready(function(){
    // start up the SocketIO connection to the server
    var socket = io.connect('http://127.0.0.1:5000/'); //'http://' + document.domain + ':' + location.port);
    socket.on('connect', function() {
        socket.emit('my event', 'Testing testing 1 2 3');
    });
    socket.on('my response', function(data) {
        document.getElementById('results').innerHTML = data;
    });
    document.getElementById("calculate").disabled = true;
});

function createMatrix() {
    var rows = document.getElementById("matrixRowsSelect").value;
    var cols = document.getElementById("matrixColsSelect").value;
    var tableWrapper1 = '<br><div class="col-md-4 col-md-offset-4"><table class="table table-sm table-bordered"><tbody>';
    var cell1 = '<input type="number" class="col-sm-10" style="margin: 5px;" id="';
    var cell2 = '">';
    var tableWrapper2 = '</tbody></table></div>';

    var adder = tableWrapper1;
    for (var i = 0; i < rows; i++) {
        adder += '<tr>';
        for (var j = 0; j < cols; j++) {
            adder += '<td>' + cell1 + i + j + cell2 + '</td>';
        }
        adder += '</tr>';
    }
    adder += tableWrapper2;
    document.getElementById('matrix').innerHTML = adder;
    document.getElementById("calculate").disabled = false;
}

function calculate() {
    document.getElementById('matrix').innerHTML = "Calculating...";
    var cells = document.getElementById('matrix').getElementsByTagName('input');
    var rows = document.getElementById("matrixRowsSelect").value;
    var cols = document.getElementById("matrixColsSelect").value;
    var func = document.getElementById("functionSelect").value;

    var vals = '{"matrix" : "[';
    // package json with rows, cols, and values sections
    for (var i = 0; i < cells.length; i++) {

    }

    if (validateMatrix()) {
        vals = "1,2,3,4,5,6,7,8,9";
        var cid = "12345";
        var test = {"clientID" : cid,
                    'func' : func,
                    "rows" : 3,
                    "cols" : 3,
                    "values" : vals};

        var socket = io.connect('http://127.0.0.1:5000/');
        socket.on('connect', function() {
            socket.emit('calculate', test);
        });
        socket.on('result', function(data) {
            document.getElementById('results').innerHTML = data;
        });


    } else {
        document.getElementById('results').innerHTML = 'Invalid matrix, bub';
    }

}

function validateMatrix() {
    return true;
}
