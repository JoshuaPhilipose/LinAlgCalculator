function createMatrix() {
    var rows = document.getElementById("matrixRowsSelect").value;
    var cols = document.getElementById("matrixColsSelect").value;
    var cell1 = '<input type="number" class="col-sm-1" style="padding: 5px;" id="';
    var cell2 = '">';
    var adder = '';

    for (var i = 0; i < rows; i++) {
        for (var j = 0; j < cols; j++) {
            adder += cell1 + i + j + cell2;
        }
        adder += '<br><br>';
    }
    document.getElementById('matrix').innerHTML = adder;
}

function calculate() {
    var matrix = [];
    var cells = document.getElementById('matrix').getElementsByTagName('input');
    var matrixJSON = '{"matrix" : "[';
    for (var i = 0; i < cells.length; i++) {

    }
    matrixJSON += ']"}';
    matrix.push(matrixJSON);
    rref(matrix)
}

function rref(matrix) {
    // ajax the JSON to the server
    $.post("rref", matrix, function(result){
        document.getElementById('results').innerHTML = result;
    });
    // stop link reloading the page
    event.preventDefault();
}