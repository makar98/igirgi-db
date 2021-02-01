function addRow(el) {
    console.log(el.parentNode.parentNode.parentNode)
    tbl = el.parentNode.parentNode.parentNode
    data_row = tbl.lastElementChild
    index = parseInt(data_row.dataset.index)

    new_data_row = document.createElement("div")
    new_data_row.innerHTML = data_row.innerHTML
    new_data_row.dataset.index = index + 1
    new_data_row.className = 'form-group row'

    tbl.appendChild(new_data_row)


    delete_button = new_data_row.lastElementChild.lastElementChild
    delete_button.style.display = 'block'

    // Нужно обращаться не ко всем datepicker, а только к новым (на текущей строке)
    // И вообще здесь нужно создавать строку, а не копировать

    $('.range_date').datepicker({position: "top right",
                                            todayButton: true,
                                            range: true,
                                            multipleDatesSeparator: " - "}
                                            )
    $(".assigned_date").datepicker({todayButton: new Date(),
                                    clearButton: true,
                                    dateFormat: "dd-mm-yyyy"}
                                    );

}