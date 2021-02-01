window.onload = $(function(){
    $(".assigned_date").datepicker({todayButton: new Date(),
                                    clearButton: true,
                                    dateFormat: "dd-mm-yyyy"});

});
