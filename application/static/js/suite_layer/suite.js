function add_suite() {
    form = document.getElementById('add_suite')
    _suite = form.querySelector('input[name="suite"]').value
    header = form.querySelector('.modal-header')


    fields_id = $('#fields').val()
    console.log(JSON.stringify(fields_id))

    var formData = new FormData(document.forms.person);
    formData.append("name", _suite);
    formData.append("fields_id", JSON.stringify(fields_id));


    var xhr = new XMLHttpRequest();
    url = 'http://' + document.location.host + '/api/suite'
    xhr.open("POST", url);
    xhr.send(formData);

    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            if(xhr.status == 200) {
                suites_div = document.getElementById('suites')
                suite = JSON.parse(xhr.responseText)

                link = document.createElement('a');
                link.setAttribute('href', '/suite/' + suite['id'])
                liFirst = document.createElement('li');
                liFirst.innerHTML = suite['name'];
                link.append(liFirst);
                suites_div.prepend(link)

                header.innerHTML = 'Свита ' + suite['name'] + ' успешно добавлена'
            }
            if(xhr.status == 400 || xhr.status == 500) {
                header.innerHTML = 'Свита не добавлена'
            }
        }
    }
}

function edit_suite() {
    check = confirm('Сохранить изменения в БД?');
    if (!check){
        return
        }
    form = document.getElementById('edit_suite')
    // _customer - from page
    // customer - response
    _suite = form.querySelector('input[name="suite"]')
    suite_name = _suite.value
    suite_id = _suite.dataset.id
    var fields_id = $('#fields').val()
    header = form.querySelector('.modal-header')

    var formData = new FormData(document.forms.person);
    formData.append("suite", suite_name);
    formData.append("fields_id", JSON.stringify(fields_id));

    var xhr = new XMLHttpRequest();
    url = 'http://' + document.location.host + '/api/suite/' + suite_id
    xhr.open("PUT", url);
    xhr.send(formData);

    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            if(xhr.status == 201) {
                suite = JSON.parse(xhr.responseText)
                _suite.value = suite['name']
                main_page_suite =  document.getElementById('suite')

                main_page_suite.innerHTML = 'Свита ' + suite['name']

                header.innerHTML = 'Успех'
            }
            if(xhr.status == 400 || xhr.status == 500) {
                header.innerHTML = 'Провал'
            }
        }
    }
}

function delete_suite() {
    check = confirm('Удалить свиту из БД?');
    if (!check){
        return
        }
    form = document.getElementById('edit_suite')
    // _customer - from page
    // customer - response
    _suite = form.querySelector('input[name="suite"]')
    suite_id = _suite.dataset.id
    header = form.querySelector('.modal-header')

    var formData = new FormData(document.forms.person);

    var xhr = new XMLHttpRequest();
    url = 'http://' + document.location.host + '/api/suite/' + suite_id
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