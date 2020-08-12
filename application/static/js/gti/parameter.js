function add_parameter() {
    form = document.getElementById('add_parameter')
    _parameter = form.querySelector('input[name="parameter"]').value
    header = form.querySelector('.modal-header')

    var formData = new FormData(document.forms.person);
    formData.append("name", _parameter);

    var xhr = new XMLHttpRequest();
    url = 'http://' + document.location.host + '/api/gti/parameter'
    xhr.open("POST", url);
    xhr.send(formData);

    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            if(xhr.status == 200) {
                parameters_div = document.getElementById('parameters')
                parameter = JSON.parse(xhr.responseText)

                link = document.createElement('a');
                link.setAttribute('href', '/gti/gti_parameter/' + parameter['id'])
                liFirst = document.createElement('li');
                liFirst.innerHTML = parameter['name'];
                link.append(liFirst);
                parameters_div.prepend(link)

                header.innerHTML = 'Параметр ' + parameter['name'] + ' успешно добавлен'
            }
            if(xhr.status == 400 || xhr.status == 500) {
                header.innerHTML = 'Параметр не добавлен'
            }
        }
    }
}

function edit_parameter() {
    check = confirm('Сохранить изменения в БД?');
    if (!check){
        return
        }
    form = document.getElementById('edit_parameter')
    // _customer - from page
    // customer - response
    _parameter = form.querySelector('input[name="parameter"]')
    parameter_name = _parameter.value
    parameter_id = _parameter.dataset.id
    header = form.querySelector('.modal-header')

    var formData = new FormData(document.forms.person);
    formData.append("name", parameter_name);

    var xhr = new XMLHttpRequest();
    url = 'http://' + document.location.host + '/api/gti/parameter/' + parameter_id
    xhr.open("PUT", url);
    xhr.send(formData);

    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            if(xhr.status == 201) {
                parameter = JSON.parse(xhr.responseText)
                _parameter.value = parameter['name']
                main_page_parameter =  document.getElementById('parameter')

                main_page_parameter.innerHTML = 'Параметр ' + parameter['name']

                header.innerHTML = 'Успех'
            }
            if(xhr.status == 400 || xhr.status == 500) {
                header.innerHTML = 'Провал'
            }
        }
    }
}

function delete_parameter() {
    check = confirm('Удалить ДО из БД?');
    if (!check){
        return
        }
    form = document.getElementById('edit_parameter')
    // _customer - from page
    // customer - response
    _parameter = form.querySelector('input[name="parameter"]')
    parameter_id = _parameter.dataset.id
    header = form.querySelector('.modal-header')

    var formData = new FormData(document.forms.person);

    var xhr = new XMLHttpRequest();
    url = 'http://' + document.location.host + '/api/gti/parameter/' + parameter_id
    xhr.open("DELETE", url);
    xhr.send(formData);

    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            if(xhr.status == 204) {
                window.location.replace('http://' + document.location.host + '/gti/parameters')
            }
            if(xhr.status == 400 || xhr.status == 500) {
                header.innerHTML = 'Провал'
            }
        }
    }
}