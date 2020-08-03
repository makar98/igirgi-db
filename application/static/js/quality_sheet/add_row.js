function addRow() {
    body_1 = document.getElementById('body_1');
    values = body_1.lastElementChild
    selected_index = values.children[0].children[0].selectedIndex
    index = parseInt(values.dataset.index) + parseInt(1)

    copy_body_1 = document.createElement("div")
    copy_body_1.innerHTML = values.innerHTML
    copy_body_1.dataset.index = index
    copy_body_1.className = 'form-group row'

    body_1.appendChild(copy_body_1)

    body_1.lastElementChild.children[0].children[0].selectedIndex = selected_index

    delete_button = body_1.lastElementChild.lastElementChild.lastElementChild
    delete_button.style.display = 'block'

    $('.range_date').datepicker({position: "top right",
                                            todayButton: true,
                                            range: true,
                                            multipleDatesSeparator: " - "}
                                            )
    $(".assigned_date").datepicker({todayButton: new Date(),
                                    clearButton: true,
                                    dateFormat: "dd-mm-yyyy"}
                                    );

    body_2 = document.getElementById('body_2');
    values = body_2.lastElementChild
    copy_body_2 = document.createElement("div")
    copy_body_2.innerHTML = values.innerHTML
    copy_body_2.dataset.index = index
    copy_body_2.className = 'form-group row'

    body_2.appendChild(copy_body_2)
}