function add_pad() {
    form = document.getElementById('add_pad')
    _pad = form.querySelector('input[name="pad"]').value
    header = form.querySelector('.modal-header')

    field = document.getElementById('field')
    field_id = field.dataset.id

    var formData = new FormData(document.forms.person);
    formData.append("name", _pad);
    console.log(_pad)
    formData.append("field_id", field_id);

    var xhr = new XMLHttpRequest();
    url = 'http://' + document.location.host + '/api/pad'
    xhr.open("POST", url);
    xhr.send(formData);

    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            if(xhr.status == 200) {
                pads_div = document.getElementById('pads')
                pad = JSON.parse(xhr.responseText)

                link = document.createElement('a');
                link.setAttribute('href', '/new_style_pad/' + pad['id'])
                liFirst = document.createElement('li');
                liFirst.innerHTML = field.value + ' ' + pad['name'];
                link.append(liFirst);
                pads_div.prepend(link)

                header.innerHTML = 'Куст ' + pad['name'] + ' успешно добавлен'
            }
            if(xhr.status == 400 || xhr.status == 500) {
                header.innerHTML = 'Куст не добавлену'
            }
        }
    }
}

function edit_pad() {
    check = confirm('Сохранить изменения в БД?');
    if (!check){
        return
        }
    form = document.getElementById('edit_pad')
    // _pad - from page
    // pad - response
    _pad = form.querySelector('input[name="pad"]')
    pad_name = _pad.value
    pad_id = _pad.dataset.id
    header = form.querySelector('.modal-header')

    var formData = new FormData(document.forms.person);
    formData.append("name", pad_name);

    var xhr = new XMLHttpRequest();
    url = 'http://' + document.location.host + '/api/pad/' + pad_id
    xhr.open("PUT", url);
    xhr.send(formData);

    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            if(xhr.status == 201) {
                pad = JSON.parse(xhr.responseText)
                _pad.value = pad['name']
                main_page_pad = document.getElementById('pad_link')
                main_page_pad.innerHTML = 'Куст <br>' + pad['name']

                header.innerHTML = 'Успех'
            }
            else {
                header.innerHTML = 'Провал'
            }
        }
    }
}

function delete_pad() {
    check = confirm('Удалить ДО из БД?');
    if (!check){
        return
        }
    form = document.getElementById('edit_pad')
    // _pad - from page
    // pad - response
    _pad = form.querySelector('input[name="pad"]')
    pad_name = _pad.value
    pad_id = _pad.dataset.id
    header = form.querySelector('.modal-header')

    var formData = new FormData(document.forms.person);

    var xhr = new XMLHttpRequest();
    url = 'http://' + document.location.host + '/api/pad/' + pad_id
    xhr.open("DELETE", url);
    xhr.send(formData);

    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            if(xhr.status == 204) {
                customer = document.getElementById('field_link')
                customer_id = customer.dataset.id
                window.location.replace('http://' + document.location.host + '/new_style_field/' + customer_id)
            }
            else {
                header.innerHTML = 'Провал'
            }
        }
    }
}