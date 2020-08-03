function add_customer() {
    form = document.getElementById('add_customer')
    _customer = form.querySelector('input[name="customer"]').value
    header = form.querySelector('.modal-header')

    var formData = new FormData(document.forms.person);
    formData.append("customer", _customer);

    var xhr = new XMLHttpRequest();
    url = 'http://' + document.location.host + '/api/customer'
    xhr.open("POST", url);
    xhr.send(formData);

    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            if(xhr.status == 200) {
                customers_div = document.getElementById('customers')
                customer = JSON.parse(xhr.responseText)

                link = document.createElement('a');
                link.setAttribute('href', '/new_style_customer/' + customer['id'])
                liFirst = document.createElement('li');
                liFirst.innerHTML = customer['name'];
                link.append(liFirst);
                customers_div.prepend(link)

                header.innerHTML = 'Заказчик ' + customer['name'] + ' успешно добавлен'
            }
            if(xhr.status == 400 || xhr.status == 500) {
                header.innerHTML = 'Заказчик не добавлен'
            }
        }
    }
}

function edit_customer() {
    check = confirm('Сохранить изменения в БД?');
    if (!check){
        return
        }
    form = document.getElementById('edit_customer')
    // _customer - from page
    // customer - response
    _customer = form.querySelector('input[name="customer"]')
    customer_name = _customer.value
    customer_id = _customer.dataset.id
    header = form.querySelector('.modal-header')

    var formData = new FormData(document.forms.person);
    formData.append("name", customer_name);

    var xhr = new XMLHttpRequest();
    url = 'http://' + document.location.host + '/api/customer/' + customer_id
    xhr.open("PUT", url);
    xhr.send(formData);

    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            if(xhr.status == 201) {
                customer = JSON.parse(xhr.responseText)
                _customer.value = customer['name']
                main_page_customer =  document.getElementById('customer')

                main_page_customer.innerHTML = 'Дочернее общество <br>' + customer['name']

                header.innerHTML = 'Успех'
            }
            if(xhr.status == 400 || xhr.status == 500) {
                header.innerHTML = 'Провал'
            }
        }
    }
}

function delete_customer() {
    check = confirm('Удалить ДО из БД?');
    if (!check){
        return
        }
    form = document.getElementById('edit_customer')
    // _customer - from page
    // customer - response
    _customer = form.querySelector('input[name="customer"]')
    customer_id = _customer.dataset.id
    header = form.querySelector('.modal-header')

    var formData = new FormData(document.forms.person);

    var xhr = new XMLHttpRequest();
    url = 'http://' + document.location.host + '/api/customer/' + customer_id
    xhr.open("DELETE", url);
    xhr.send(formData);

    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            if(xhr.status == 204) {
                window.location.replace('http://' + document.location.host + '/new_style_customers')
            }
            if(xhr.status == 400 || xhr.status == 500) {
                header.innerHTML = 'Провал'
            }
        }
    }
}