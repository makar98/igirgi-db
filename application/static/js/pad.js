function add_pad() {
    form = document.getElementById('add_pad')
    _pad = form.querySelector('input[name="pad"]').value
    header = form.querySelector('.modal-header')

    field = document.getElementById('field')
    field_id = field.dataset.id

    var formData = new FormData(document.forms.person);
    formData.append("pad", _pad);
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