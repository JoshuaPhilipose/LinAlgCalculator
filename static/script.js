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

// window.onload = function() {
//     // setup the button click
//     document.getElementById("calculate").onclick = function() {
//         calculate()
//     };
// }

function calculate() {
    document.getElementById('results').innerHTML = "Calculating...";
    var matrix = [];
    // var cells = document.getElementById('matrix').getElementsByTagName('input');
    // var matrixJSON = '{"matrix" : "[';
    //package json with rows, cols, and values sections
    // for (var i = 0; i < cells.length; i++) {
    //
    // }
    // matrixJSON += ']"}';
    // matrix.push(matrixJSON);
    var test = '{"rows" : 3, "cols" : 3, "values" : "1,2,3,4,5,6,7,8,9"}'
    matrix.push(test);

    // ajax the JSON to the server CLEARLY NOT WORKING
    // $.post("rref", matrix);
    // rref(matrix);
}

// function rref(matrix) {
    // document.getElementById('results').innerHTML = result;
    // stop link reloading the page
    // event.preventDefault();
    // var resultMatrix = '{{ RREFresult }}'; //= '[0]'
    // document.getElementById('results').innerHTML = resultMatrix;
// }