function add_field() {
    form = document.getElementById('add_field')
    _field = form.querySelector('input[name="field"]').value
    header = form.querySelector('.modal-header')

    customer_id = document.getElementById('customer').dataset.id
    console.log(header)

    var formData = new FormData(document.forms.person);
    formData.append("name", _field);
    formData.append("customer_id", customer_id);

    var xhr = new XMLHttpRequest();
    url = 'http://' + document.location.host + '/api/field'
    xhr.open("POST", url);
    xhr.send(formData);

    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            if(xhr.status == 200) {
                fields_div = document.getElementById('fields')
                field = JSON.parse(xhr.responseText)

                link = document.createElement('a');
                link.setAttribute('href', '/new_style_field/' + field['id'])
                liFirst = document.createElement('li');
                liFirst.innerHTML = field['name'];
                link.append(liFirst);
                fields_div.prepend(link)

                header.innerHTML = 'Месторождение ' + field['name'] + ' успешно добавлено'
            }
            if(xhr.status == 400 || xhr.status == 500) {
                header.innerHTML = 'Месторождение не добавлено'
            }
        }
    }
}

function edit_field() {
    check = confirm('Сохранить изменения в БД?');
    if (!check){
        return
        }
    form = document.getElementById('edit_field')
    // _field - from page
    // field - response
    _field = form.querySelector('input[name="field"]')
    field_name = _field.value
    field_id = _field.dataset.id
    header = form.querySelector('.modal-header')

    var formData = new FormData(document.forms.person);
    formData.append("name", field_name);

    var xhr = new XMLHttpRequest();
    url = 'http://' + document.location.host + '/api/field/' + field_id
    xhr.open("PUT", url);
    xhr.send(formData);

    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            if(xhr.status == 201) {
                field = JSON.parse(xhr.responseText)
                _field.value = field['name']
                main_page_field = document.getElementById('field_link')
                main_page_field.innerHTML = 'Месторождение <br>' + field['name']

                header.innerHTML = 'Успех'
            }
            if(xhr.status == 400 || xhr.status == 500) {
                header.innerHTML = 'Провал'
            }
        }
    }
}

function delete_field() {
    check = confirm('Удалить ДО из БД?');
    if (!check){
        return
        }
    form = document.getElementById('edit_field')
    // _field - from page
    // field - response
    _field = form.querySelector('input[name="field"]')
    field_name = _field.value
    field_id = _field.dataset.id
    header = form.querySelector('.modal-header')

    var formData = new FormData(document.forms.person);

    var xhr = new XMLHttpRequest();
    url = 'http://' + document.location.host + '/api/field/' + field_id
    xhr.open("DELETE", url);
    xhr.send(formData);

    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            if(xhr.status == 204) {
                customer = document.getElementById('customer_link')
                customer_id = customer.dataset.id
                window.location.replace('http://' + document.location.host + '/new_style_customer/' + customer_id)
            }
            if(xhr.status == 400 || xhr.status == 500) {
                header.innerHTML = 'Провал'
            }
        }
    }
}