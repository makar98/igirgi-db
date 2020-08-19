function add_company() {
    form = document.getElementById('add_company')
    _company = form.querySelector('input[name="company"]').value
    header = form.querySelector('.modal-header')

    var formData = new FormData(document.forms.person);
    formData.append("name", _company);

    var xhr = new XMLHttpRequest();
    url = 'http://' + document.location.host + '/api/gti/company'
    xhr.open("POST", url);
    xhr.send(formData);

    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            if(xhr.status == 200) {
                companies_div = document.getElementById('companies')
                company = JSON.parse(xhr.responseText)

                link = document.createElement('a');
                link.setAttribute('href', '/gti/directory/service_company/' + company['id'])
                liFirst = document.createElement('li');
                liFirst.innerHTML = company['name'];
                link.append(liFirst);
                companies_div.prepend(link)

                header.innerHTML = 'Подрядчик ' + company['name'] + ' успешно добавлен'
            }
            if(xhr.status == 400 || xhr.status == 500) {
                header.innerHTML = 'Подрядчик не добавлен'
            }
        }
    }
}

function edit_company() {
    check = confirm('Сохранить изменения в БД?');
    if (!check){
        return
        }
    form = document.getElementById('edit_company')
    // _customer - from page
    // customer - response
    _company = form.querySelector('input[name="company"]')
    company_name = _company.value
    company_id = _company.dataset.id
    header = form.querySelector('.modal-header')

    var formData = new FormData(document.forms.person);
    formData.append("name", company_name);

    var xhr = new XMLHttpRequest();
    url = 'http://' + document.location.host + '/api/gti/company/' + company_id
    xhr.open("PUT", url);
    xhr.send(formData);

    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            if(xhr.status == 201) {
                company = JSON.parse(xhr.responseText)
                _company.value = company['name']
                main_page_company =  document.getElementById('company')

                main_page_company.innerHTML = 'Параметр ' + company['name']

                header.innerHTML = 'Успех'
            }
            if(xhr.status == 400 || xhr.status == 500) {
                header.innerHTML = 'Провал'
            }
        }
    }
}

function delete_company() {
    check = confirm('Удалить ДО из БД?');
    if (!check){
        return
        }
    form = document.getElementById('edit_company')
    // _customer - from page
    // customer - response
    _company = form.querySelector('input[name="company"]')
    company_id = _company.dataset.id
    header = form.querySelector('.modal-header')

    var formData = new FormData(document.forms.person);

    var xhr = new XMLHttpRequest();
    url = 'http://' + document.location.host + '/api/gti/company/' + company_id
    xhr.open("DELETE", url);
    xhr.send(formData);

    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            if(xhr.status == 204) {
                window.location.replace('http://' + document.location.host + '/gti/directory/service_companies')
            }
            if(xhr.status == 400 || xhr.status == 500) {
                header.innerHTML = 'Провал'
            }
        }
    }
}