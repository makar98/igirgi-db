function add_format() {
    form = document.getElementById('add_format')
    _format = form.querySelector('input[name="format"]').value
    header = form.querySelector('.modal-header')

    parameter_id = document.getElementById('parameter').dataset.id

    var formData = new FormData(document.forms.person);
    formData.append("name", _format);
    formData.append("parameter_id", parameter_id);

    var xhr = new XMLHttpRequest();
    url = 'http://' + document.location.host + '/api/gti/format'
    xhr.open("POST", url);
    xhr.send(formData);

    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            if(xhr.status == 200) {
                formats_div = document.getElementById('formats')
                format = JSON.parse(xhr.responseText)

                link = document.createElement('a');
                link.setAttribute('href', '/gti/format/' + format['id'])
                liFirst = document.createElement('li');
                liFirst.innerHTML = format['name'];
                link.append(liFirst);
                formats_div.prepend(link)

                header.innerHTML = 'Формат ' + format['name'] + ' успешно добавлен'
            }
            if(xhr.status == 400 || xhr.status == 500) {
                header.innerHTML = 'Формат не добавлен'
            }
        }
    }
}

function edit_format() {
    check = confirm('Сохранить изменения в БД?');
    if (!check){
        return
        }
    form = document.getElementById('edit_format')
    // _customer - from page
    // customer - response
    _format = form.querySelector('input[name="format"]')
    format_name = _format.value
    format_id = _format.dataset.id
    header = form.querySelector('.modal-header')

    var formData = new FormData(document.forms.person);
    formData.append("name", format_name);

    var xhr = new XMLHttpRequest();
    url = 'http://' + document.location.host + '/api/gti/format/' + format_id
    xhr.open("PUT", url);
    xhr.send(formData);

    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            if(xhr.status == 201) {
                format = JSON.parse(xhr.responseText)
                _format.value = format['name']
                main_page_format =  document.getElementById('format')

                main_page_format.innerHTML = 'Параметр ' + format['name']

                header.innerHTML = 'Успех'
            }
            if(xhr.status == 400 || xhr.status == 500) {
                header.innerHTML = 'Провал'
            }
        }
    }
}

function delete_format() {
    check = confirm('Удалить ДО из БД?');
    if (!check){
        return
        }
    form = document.getElementById('edit_format')
    // _customer - from page
    // customer - response
    _format = form.querySelector('input[name="format"]')
    format_id = _format.dataset.id
    header = form.querySelector('.modal-header')

    var formData = new FormData(document.forms.person);

    var xhr = new XMLHttpRequest();
    url = 'http://' + document.location.host + '/api/gti/format/' + format_id
    xhr.open("DELETE", url);
    xhr.send(formData);

    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            if(xhr.status == 204) {
                parameter_id = document.getElementById('parameter').dataset.id
                window.location.replace('http://' + document.location.host + '/gti/parameter/' + parameter_id)
            }
            if(xhr.status == 400 || xhr.status == 500) {
                header.innerHTML = 'Провал'
            }
        }
    }
}