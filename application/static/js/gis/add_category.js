function add_category() {
    form = document.getElementById('add-category')
    header = form.querySelector('.modal-header')
    _category = form.querySelector('input[name="category"]').value

    var formData = new FormData();
    formData.append("category", _category);

    var xhr = new XMLHttpRequest();
    url = 'http://' + document.location.host + '/api/gis_category'
    xhr.open("POST", url);
    xhr.send(formData);

    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            if(xhr.status == 200) {
                category = JSON.parse(xhr.responseText)

                header.innerHTML = 'Раздел ' + category['name'] + ' успешно добавлен'
            }
            if(xhr.status == 400 || xhr.status == 500) {
                header.innerHTML = 'Заказчик не добавлен'
            }
        }
    }
}