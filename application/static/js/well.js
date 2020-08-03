function add_well() {
    form = document.getElementById('add_well')
    header = form.querySelector('.modal-header')

    customer_id = form.querySelector('input[name="customer"]').dataset.id
    field_id = form.querySelector('input[name="field"]').dataset.id
    pad_id = form.querySelector('input[name="pad"]').dataset.id

    well_type_form = form.querySelector('select[name="well_type"]')
    well_type_index = well_type_form.selectedIndex
    well_type_id = well_type_form[well_type_index].dataset.id

     _well = form.querySelector('input[name="well"]').value

    var formData = new FormData(document.forms.person);
    formData.append("customer_id", customer_id);
    formData.append("field_id", field_id);
    formData.append("pad_id", pad_id);
    formData.append("well", _well);
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
                liFirst.innerHTML = well['name'];
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
