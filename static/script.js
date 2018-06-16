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
    var calculateButton = ''
}

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

    if (validateMatrix()) {
        var matrixData = {
            // "first_name": $("#first_name").val(),
            // "last_name": $("#last_name").val(),
            // "gt_id": $("#gtid").val(),
            // "num_rush_nights": 1,
            // "email": $("#email").val(),
            // "major": $("#major").val(),
            // "year": $("#year").val(),
            // "phone_no": $("#phonenumber").val(),
            // "texting": $("#cantext").val(),
            // "dorm": $("#residence").val(),
            // "rush_buddy": $("#buddy").val(),
            // "rush_source": $("#howhear").val(),
            // "akpsi_friend": $("#AKPsiFriendName").val(),
            // "other_input": $("#OtherInput").val(),
            "photo_url": "",
            "status": "Mid-Cloud",
            "rush_night_2": "true"
        };
        var test = {"rows" : 3, "cols" : 3, "values" : "1,2,3,4,5,6,7,8,9"};
        matrix.push(test);

        // MUST PUT FULL URL
        $.ajax({
            url: 'http://127.0.0.1:5000/rref',
            type: 'POST',
            data: JSON.stringify(test),
            success: function(data) {
                document.getElementById('results').innerHTML = "Success";
            }
        });

    } else {
        document.getElementById('results').innerHTML = 'Invalid matrix, bub';
    }

}

function validateMatrix() {
    return true;
}
