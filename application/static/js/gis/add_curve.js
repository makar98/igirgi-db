function add_curve() {
    form = document.getElementById('add-curve')
    header = form.querySelector('.modal-header')

    _method = form.querySelector('input[name="method"]').value

    category = form.querySelector('select[name="category"]')
    category_index = category.selectedIndex
    category_id = category[category_index].dataset.id

    latin = form.querySelector('input[name="latin"]').value
    curve_type = form.querySelector('input[name="curve_type"]').value
    units = form.querySelector('input[name="units"]').value
    notes = form.querySelector('input[name="notes"]').value

    var formData = new FormData();
    formData.append("method", _method);
    formData.append("category_id", category_id);
    formData.append("latin", latin);
    formData.append("curve_type", curve_type);
    formData.append("units", units);
    formData.append("notes", notes);

    var xhr = new XMLHttpRequest();
    url = 'http://' + document.location.host + '/api/gis_curve'
    xhr.open("POST", url);
    xhr.send(formData);

    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            if(xhr.status == 200) {
                curve = JSON.parse(xhr.responseText)

                header.innerHTML = 'Метод ' + curve['name'] + ' успешно добавлен'
            }
            if(xhr.status == 400 || xhr.status == 500) {
                header.innerHTML = 'Метод НЕ добавлен'
            }
        }
    }
}
