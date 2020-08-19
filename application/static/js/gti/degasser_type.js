function add_type() {
    form = document.getElementById('add_type')
    _type = form.querySelector('input[name="type"]').value
    header = form.querySelector('.modal-header')

    var formData = new FormData(document.forms.person);
    formData.append("name", _type);

    var xhr = new XMLHttpRequest();
    url = 'http://' + document.location.host + '/api/gti/degasser_type'
    xhr.open("POST", url);
    xhr.send(formData);

    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            if(xhr.status == 200) {
                types_div = document.getElementById('types')
                type = JSON.parse(xhr.responseText)

                link = document.createElement('a');
                link.setAttribute('href', '/gti/directory/degasser_type/' + type['id'])
                liFirst = document.createElement('li');
                liFirst.innerHTML = type['name'];
                link.append(liFirst);
                types_div.prepend(link)

                header.innerHTML = 'Тип ' + type['name'] + ' успешно добавлен'
            }
            if(xhr.status == 400 || xhr.status == 500) {
                header.innerHTML = 'Тип не добавлен'
            }
        }
    }
}

function edit_type() {
    check = confirm('Сохранить изменения в БД?');
    if (!check){
        return
        }
    form = document.getElementById('edit_type')
    // _customer - from page
    // customer - response
    _type = form.querySelector('input[name="type"]')
    type_name = _type.value
    type_id = _type.dataset.id
    header = form.querySelector('.modal-header')

    var formData = new FormData(document.forms.person);
    formData.append("name", type_name);

    var xhr = new XMLHttpRequest();
    url = 'http://' + document.location.host + '/api/gti/degasser_type/' + type_id
    console.log(url)
    xhr.open("PUT", url);
    xhr.send(formData);

    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            if(xhr.status == 201) {
                type = JSON.parse(xhr.responseText)
                _type.value = type['name']
                main_page_type =  document.getElementById('type')

                main_page_type.innerHTML = 'Тип станции ' + type['name']

                header.innerHTML = 'Успех'
            }
            if(xhr.status == 400 || xhr.status == 500) {
                header.innerHTML = 'Провал'
            }
        }
    }
}

function delete_type() {
    check = confirm('Удалить ДО из БД?');
    if (!check){
        return
        }
    form = document.getElementById('edit_type')
    // _customer - from page
    // customer - response
    _type = form.querySelector('input[name="type"]')
    type_id = _type.dataset.id
    header = form.querySelector('.modal-header')

    var formData = new FormData(document.forms.person);

    var xhr = new XMLHttpRequest();
    url = 'http://' + document.location.host + '/api/gti/degasser_type/' + type_id
    xhr.open("DELETE", url);
    xhr.send(formData);

    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            if(xhr.status == 204) {
                window.location.replace('http://' + document.location.host + '/gti/directory/degasser_type')
            }
            if(xhr.status == 400 || xhr.status == 500) {
                header.innerHTML = 'Провал'
            }
        }
    }
}