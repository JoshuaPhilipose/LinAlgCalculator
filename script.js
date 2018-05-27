function createMatrix() {
    var rows = document.getElementById("matrixRowsSelect").value;
    var cols = document.getElementById("matrixColsSelect").value;
    var cell1 = '<input type="number" class="col-sm-1" style="padding: 5px;" id="'
    var cell2 = '">'
    var adder = ''

    for (var i = 0; i < rows; i++) {
        for (var j = 0; j < cols; j++) {
            adder += cell1 + i + j + cell2
        }
        adder += '<br><br>'
    }
    document.getElementById('matrix').innerHTML = adder;
}
