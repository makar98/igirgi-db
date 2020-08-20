function add_well() {
    form = document.getElementById('add_well')
    _pad = form.querySelector('select[name="pad"]').value
    header = form.querySelector('.modal-header')

    customer_id = form.querySelector('input[name="customer"]').dataset.id

    _field_opt = form.querySelector('select[name="field"]')
    field_name = _field_opt.value
    _field_index = form.querySelector('select[name="field"]').selectedIndex
    field_id = _field_opt[_field_index].dataset.id

    _pad_opt = form.querySelector('select[name="pad"]')
    pad_name = _pad_opt.value
    _pad_index = form.querySelector('select[name="pad"]').selectedIndex
    pad_id = _pad_opt[_pad_index].dataset.id

    well_type_form = form.querySelector('select[name="well_type"]')
    well_type_index = well_type_form.selectedIndex
    well_type_id = well_type_form[well_type_index].dataset.id

     _well = form.querySelector('input[name="well"]').value

    var formData = new FormData(document.forms.person);
    formData.append("customer_id", customer_id);
    formData.append("field_id", field_id);
    formData.append("pad_id", pad_id);
    formData.append("name", _well);
    formData.append("well_type_id", well_type_id);

    var xhr = new XMLHttpRequest();
    url = 'http://' + document.location.host + '/api/well'
    xhr.open("POST", url);
    xhr.send(formData);

    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            if(xhr.status == 200) {
                wells_div = document.getElementById('wells')
                well = JSON.parse(xhr.responseText)

                //link = document.createElement('a');
                //link.setAttribute('href', '/new_style_pad/' + well['id'])
                liFirst = document.createElement('li');
                liFirst.innerHTML = field_name + ' Куст ' + pad_name + ' Скважина ' + well['name'];
                //link.append(liFirst);
                //wells_div.prepend(link)
                wells_div.prepend(liFirst)

                header.innerHTML = 'Скважина ' + well['name'] + ' успешно добавлена'
            }
            if(xhr.status == 400 || xhr.status == 500) {
                header.innerHTML = 'Скважина НЕ добавлена'
            }
        }
    }
}

function get_pads() {
    form = document.getElementById('add_well')
    _field_opt = form.querySelector('select[name="field"]')
    _index = form.querySelector('select[name="field"]').selectedIndex
    field_id = _field_opt[_index].dataset.id

    opt = form.querySelector('select[name="pad"]')

    pad_xhr = new XMLHttpRequest();
    url = 'http://' + document.location.host + '/api/field/' + field_id
    pad_xhr.open("GET", url);
    pad_xhr.send();

    pad_xhr.onreadystatechange = function() {
        if (pad_xhr.readyState == 4) {
            if(pad_xhr.status == 200) {
                field = JSON.parse(pad_xhr.responseText)
                // Удаление старых option
                opt.length = 0;
                opt.options[0] = new Option();
                i = 1
                for (pad of field['pads']){
                    opt.options[i] = new Option(pad['name']);
                    opt.options[i].setAttribute('data-id', pad['id'])
                    i++
                }
            }
        }
    }
}