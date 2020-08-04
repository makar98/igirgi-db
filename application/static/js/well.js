function add_well() {
    form = document.getElementById('add_well')
    header = form.querySelector('.modal-header')

    customer_id = form.querySelector('input[name="customer"]').dataset.id
    field_id = form.querySelector('input[name="field"]').dataset.id
    pad_id = form.querySelector('input[name="pad"]').dataset.id

    well_type_form = form.querySelector('select[name="well_type"]')
    well_type_index = well_type_form.selectedIndex
    well_type_id = well_type_form[well_type_index].dataset.id

     _well = form.querySelector('input[name="well"]').value

    var formData = new FormData(document.forms.person);
    formData.append("customer_id", customer_id);
    formData.append("field_id", field_id);
    formData.append("pad_id", pad_id);
    formData.append("well", _well);
    formData.append("well_type_id", well_type_id);

    var xhr = new XMLHttpRequest();
    url = 'http://' + document.location.host + '/api/well'
    xhr.open("POST", url);
    xhr.send(formData);

    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            if(xhr.status == 200) {
                wells_div = document.getElementById('wells')
                well = JSON.parse(xhr.responseText)

                //link = document.createElement('a');
                //link.setAttribute('href', '/new_style_pad/' + well['id'])
                liFirst = document.createElement('li');
                liFirst.innerHTML = well['name'];
                //link.append(liFirst);
                //wells_div.prepend(link)
                wells_div.prepend(liFirst)

                header.innerHTML = 'Скважина ' + well['name'] + ' успешно добавлена'
            }
            else {
                header.innerHTML = 'Скважина НЕ добавлена'
            }
        }
    }
}


function edit_well() {
    check = confirm('Сохранить изменения в БД?');
    if (!check){
        return
        }
    form = document.getElementById('edit_well')
    // _well - from page
    // well - response
    _well = form.querySelector('input[name="well"]')
    well_name = _well.value
    well_id = _well.dataset.id

    _well_type = form.querySelector('select[name="well_type"]')
    _well_type_selectedIndex = _well_type.selectedIndex
    _well_type_name = _well_type[_well_type_selectedIndex].value
    _well_type_id = _well_type[_well_type_selectedIndex].dataset.id


    header = form.querySelector('.modal-header')

    var formData = new FormData(document.forms.person);
    formData.append("name", well_name);
    formData.append("well_type_id", _well_type_id);

    var xhr = new XMLHttpRequest();
    url = 'http://' + document.location.host + '/api/well/' + well_id
    xhr.open("PUT", url);
    xhr.send(formData);

    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            if(xhr.status == 201) {
                well = JSON.parse(xhr.responseText)
                _well.value = well['name']
                main_page_well = document.getElementById('well_link')

                well_type = (well['well_type']) ? well['well_type'] : _well_type_name
                main_page_well.innerHTML = 'Скважина <br>' + well['name'] + ' ' + well_type

                header.innerHTML = 'Успех'
            }
            else {
                header.innerHTML = 'Провал'
            }
        }
    }
}

function delete_well() {
    check = confirm('Удалить скважину из БД?');
    if (!check){
        return
        }
    form = document.getElementById('edit_well')
    // _well - from page
    // well - response
    _well = form.querySelector('input[name="well"]')
    well_name = _well.value
    well_type = _well.dataset.type
    well_id = _well.dataset.id
    header = form.querySelector('.modal-header')

    var formData = new FormData(document.forms.person);

    var xhr = new XMLHttpRequest();
    url = 'http://' + document.location.host + '/api/well/' + well_id
    xhr.open("DELETE", url);
    xhr.send(formData);
///////////////////////////////////////////////////////////
// Переделать
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            if(xhr.status == 204) {
                pad = document.getElementById('pad')
                pad_id = pad.dataset.id
                window.location.replace('http://' + document.location.host + '/new_style_pad/' + pad_id)
            }
            else {
                header.innerHTML = 'Провал'
            }
        }
    }
}