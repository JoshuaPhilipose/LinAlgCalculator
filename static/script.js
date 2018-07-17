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
    var cell1 = '<input type="text" class="col-sm-10" style="margin: 5px;" id="';
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
    var cells = document.getElementById('matrix').getElementsByTagName('input');
    var rows = document.getElementById("matrixRowsSelect").value;
    var cols = document.getElementById("matrixColsSelect").value;
    var func = document.getElementById('selectionText').innerHTML.substring(10);


    if (validateMatrix()) {
        var vals = collectValues(rows, cols);
        var cid = "12345";
        var test = {"clientID" : cid,
                    'func' : func,
                    "rows" : rows,
                    "cols" : cols,
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
    return true; // lol
}

function collectValues(rows, cols) {
    var values = "";
    for (var r = 0; r < rows; r++) {
        for (var c = 0; c < cols; c++) {
            var cellID = "" + r + c;
            values += document.getElementById(cellID).value + ",";
        }
    }
    return values;
}

function changeFunction(func) {
    document.getElementById('selectionText').innerHTML = "Selected: " + func;
}