function addRow() {
    $(".assigned_date").datepicker("destroy");

    var body_1 = document.getElementById('body_1');
    var body_2 = document.getElementById('body_2');

    var newRow_body_1 = body_1.insertRow();
    var newRow_body_2 = body_2.insertRow();

    var body_1_rows = body_1.rows;
    var body_1_prev_row = body_1_rows[body_1_rows.length-3]

    var body_2_rows = body_2.rows;
    var body_2_prev_row = body_2_rows[body_2_rows.length-2]


    for (i=0; i< 9; i++){
      var newCell_body_1 = newRow_body_1.insertCell();
      newCell_body_1.style.background = '#FAF0C8';
      newCell_body_1.style.border = "none"
      newCell_body_1.style.borderBottom = "1px solid #FFFFFF";
      newCell_body_1.style.borderRight = "1px solid #FFFFFF"

      var newCell_body_2 = newRow_body_2.insertCell();
      newCell_body_2.style.background = '#FAF0C8';
      newCell_body_2.style.border = "none"
      newCell_body_2.style.borderBottom = "1px solid #FFFFFF";
      newCell_body_2.style.borderRight = "1px solid #FFFFFF";

      var ta = document.createElement('div');
      var cal = document.createElement('input');
      cal.type = "text";
      cal.id = 'cal';
      cal.className = 'assigned_date';
      //cal.className = "datepicker-here datepicker_recurring_start";
      $('#aaa').datepicker()

      newCell_body_1.append(cal);
      };
    $(".assigned_date").datepicker({dateFormat: "yy-mm-dd"});
    }
