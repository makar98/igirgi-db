function add_well() {
    form = document.getElementById('add_well')
    _well = form.querySelector('input[name="well"]').value
    header = form.querySelector('.modal-header')

    field = document.getElementById('field')
    field_id = field.dataset.id
    field_name = field.value

    _pad_opt = form.querySelector('select[name="pad"]')
    pad_name = _pad_opt.value
    _pad_index = form.querySelector('select[name="pad"]').selectedIndex
    pad_id = _pad_opt[_pad_index].dataset.id

    well_type_form = form.querySelector('select[name="well_type"]')
    well_type_index = well_type_form.selectedIndex
    well_type_id = well_type_form[well_type_index].dataset.id

    customer = document.getElementById('customer')
    customer_id = customer.dataset.id

    var formData = new FormData(document.forms.person);
    formData.append("customer_id", customer_id);
    formData.append("field_id", field_id);
    formData.append("pad_id", pad_id);
    formData.append("well_type_id", well_type_id);
    formData.append("well", _well);

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