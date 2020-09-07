function add_layer() {
    form = document.getElementById('add_layer')
    _layer = form.querySelector('input[name="layer"]').value
    header = form.querySelector('.modal-header')

    suite_id = document.getElementById('suite').dataset.id

    var formData = new FormData(document.forms.person);

    formData.append("name", _layer);
    formData.append("suite_id", suite_id);

    var xhr = new XMLHttpRequest();
    url = 'http://' + document.location.host + '/api/layer'
    xhr.open("POST", url);
    xhr.send(formData);

    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            if(xhr.status == 200) {
                layers_div = document.getElementById('layers')
                layer = JSON.parse(xhr.responseText)

                link = document.createElement('a');
                link.setAttribute('href', '/layer/' + layer['id'])
                liFirst = document.createElement('li');
                liFirst.innerHTML = layer['name'];
                link.append(liFirst);
                layers_div.prepend(link)

                header.innerHTML = 'Пласт ' + layer['name'] + ' успешно добавлен'
            }
            if(xhr.status == 400 || xhr.status == 500) {
                header.innerHTML = 'Пласт не добавлен'
            }
        }
    }
}

function edit_layer() {
    check = confirm('Сохранить изменения в БД?');
    if (!check){
        return
        }
    form = document.getElementById('edit_layer')
    // _customer - from page
    // customer - response
    _layer = form.querySelector('input[name="layer"]')
    layer_name = _layer.value
    layer_id = _layer.dataset.id
    header = form.querySelector('.modal-header')

    var formData = new FormData(document.forms.person);
    formData.append("name", layer_name);

    var xhr = new XMLHttpRequest();
    url = 'http://' + document.location.host + '/api/layer/' + layer_id
    xhr.open("PUT", url);
    xhr.send(formData);

    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            if(xhr.status == 201) {
                layer = JSON.parse(xhr.responseText)
                _layer.value = layer['name']
                main_page_layer =  document.getElementById('layer')

                main_page_layer.innerHTML = 'Пласт ' + layer['name']

                header.innerHTML = 'Успех'
            }
            if(xhr.status == 400 || xhr.status == 500) {
                header.innerHTML = 'Провал'
            }
        }
    }
}

function delete_layer() {
    check = confirm('Удалить пласт из БД?');
    if (!check){
        return
        }
    form = document.getElementById('edit_layer')
    // _customer - from page
    // customer - response
    _layer = form.querySelector('input[name="layer"]')
    layer_id = _layer.dataset.id
    header = form.querySelector('.modal-header')

    var formData = new FormData(document.forms.person);

    var xhr = new XMLHttpRequest();
    url = 'http://' + document.location.host + '/api/layer/' + layer_id
    xhr.open("DELETE", url);
    xhr.send(formData);

    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            if(xhr.status == 204) {
                window.location.replace('http://' + document.location.host + '/suites')
            }
            if(xhr.status == 400 || xhr.status == 500) {
                header.innerHTML = 'Провал'
            }
        }
    }
}