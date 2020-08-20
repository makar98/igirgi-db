function add_pad() {
    form = document.getElementById('add_pad')
    _pad = form.querySelector('input[name="pad"]').value
    header = form.querySelector('.modal-header')

    _field_opt = form.querySelector('select[name="field"]')
    _index = form.querySelector('select[name="field"]').selectedIndex
    field_id = _field_opt[_index].dataset.id

    var formData = new FormData(document.forms.person);
    formData.append("name", _pad);
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
                liFirst.innerHTML = pad['name'];
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