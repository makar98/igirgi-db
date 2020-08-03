function add_rename_curve() {
    form = document.getElementById('add-latin')
    header = form.querySelector('.modal-header')

    curve_id = form.querySelector('input[name="method"]').dataset.id

    latin = form.querySelector('input[name="latin"]').value

    var formData = new FormData();
    formData.append("curve_id", curve_id);
    formData.append("latin", latin);

    var xhr = new XMLHttpRequest();
    url = 'http://' + document.location.host + '/api/gis_rename_curve'
    xhr.open("POST", url);
    xhr.send(formData);

    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            if(xhr.status == 200) {
                latin = JSON.parse(xhr.responseText)

                header.innerHTML = 'Сокращение ' + latin['name'] + ' успешно добавленно'
            }
            if(xhr.status == 400 || xhr.status == 500) {
                header.innerHTML = 'Сокращение НЕ добавленно'
            }
        }
    }
}
