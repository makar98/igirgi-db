function add_wellbore() {
    user = document.getElementById('user')
    user_id = user.dataset.id

    form = document.getElementById('add_wellbore')
    header = form.querySelector('.modal-header')

    well_id = form.querySelector('input[name="well"]').dataset.id

    wellbore = form.querySelector('input[name="wellbore"]').value

    let is_gis = (form.querySelector('input[name="is_gis"]').checked) ? 1 : 0;
    let is_gti = (form.querySelector('input[name="is_gti"]').checked) ? 1 : 0;

    wellbore_type_form = form.querySelector('select[name="wellbore_type"]')
    wellbore_type_index = wellbore_type_form.selectedIndex
    wellbore_type_id = wellbore_type_form[wellbore_type_index].dataset.id

    var formData = new FormData(document.forms.person);

    formData.append("user_id", user_id);
    formData.append("well_id", well_id);
    formData.append("name", wellbore);
    formData.append("wellbore_type_id", wellbore_type_id);
    formData.append("is_gis", is_gis);
    formData.append("is_gti", is_gti);

    var xhr = new XMLHttpRequest();
    url = 'http://' + document.location.host + '/api/wellbore'
    xhr.open("POST", url);
    xhr.send(formData);

    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            if(xhr.status == 200) {
                wellbores_div = document.getElementById('wellbores')
                wellbore = JSON.parse(xhr.responseText)

                link = document.createElement('a');
                link.setAttribute('href', '/new_style_wellbore/' + wellbore['id'])
                liFirst = document.createElement('li');
                liFirst.innerHTML = wellbore['name'] + ' ' + wellbore['wellbore_type']['name'];
                link.append(liFirst);

                wellbores_div.prepend(link)

                header.innerHTML = 'Секция ' + wellbore['name'] + ' успешно добавлена'
            }
            if(xhr.status == 400 || xhr.status == 500) {
                header.innerHTML = 'Секция НЕ добавлена'
            }
        }
    }
}

function edit_wellbore() {
    check = confirm('Сохранить изменения в БД?');
    if (!check){
        return
        }
    form = document.getElementById('edit_wellbore')
    // _well - from page
    // well - response
    _wellbore = form.querySelector('input[name="wellbore"]')
    wellbore_name = _wellbore.value
    wellbore_id = _wellbore.dataset.id

    _wellbore_type = form.querySelector('select[name="wellbore_type"]')
    _wellbore_type_selectedIndex = _wellbore_type.selectedIndex
    _wellbore_type_name = _wellbore_type[_wellbore_type_selectedIndex].value
    _wellbore_type_id = _wellbore_type[_wellbore_type_selectedIndex].dataset.id

    let is_gis = (form.querySelector('input[name="is_gis"]').checked) ? 1 : 0;
    let is_gti = (form.querySelector('input[name="is_gti"]').checked) ? 1 : 0;

    var layers_id = $('#layers').val()

    header = form.querySelector('.modal-header')

    var formData = new FormData(document.forms.person);
    formData.append("name", wellbore_name);
    formData.append("wellbore_type_id", _wellbore_type_id);
    formData.append("layers_id", JSON.stringify(layers_id));
    formData.append("is_gis", is_gis);
    formData.append("is_gti", is_gti);

    var xhr = new XMLHttpRequest();
    url = 'http://' + document.location.host + '/api/wellbore/' + wellbore_id
    xhr.open("PUT", url);
    xhr.send(formData);

    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            if(xhr.status == 201) {
                wellbore = JSON.parse(xhr.responseText)
                _wellbore.value = wellbore['name']
                main_page_wellbore = document.getElementById('wellbore_link')

                wellbore_type = (wellbore['well_type']) ? wellbore['well_type'] : _wellbore_type_name
                main_page_wellbore.innerHTML = 'Ствол <br>' + wellbore['name'] + ' ' + wellbore_type

                header.innerHTML = 'Успех'
            }
            else {
                header.innerHTML = 'Провал'
            }
        }
    }
}

function delete_wellbore() {
    check = confirm('Удалить ствол из БД?');
    if (!check){
        return
        }
    form = document.getElementById('edit_wellbore')
    // _well - from page
    // well - response
    _wellbore = form.querySelector('input[name="wellbore"]')
    wellbore_name = _wellbore.value
    wellbore_type = _wellbore.dataset.type
    wellbore_id = _wellbore.dataset.id
    header = form.querySelector('.modal-header')

    var formData = new FormData(document.forms.person);

    var xhr = new XMLHttpRequest();
    url = 'http://' + document.location.host + '/api/wellbore/' + wellbore_id
    xhr.open("DELETE", url);
    xhr.send(formData);

    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            if(xhr.status == 204) {
                well = document.getElementById('well')
                well_id = well.dataset.id
                window.location.replace('http://' + document.location.host + '/new_style_well/' + well_id)
            }
            else {
                header.innerHTML = 'Провал'
            }
        }
    }
}