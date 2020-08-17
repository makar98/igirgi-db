function add_wellbore() {
    user = document.getElementById('user')
    user_id = user.dataset.id

    form = document.getElementById('add_wellbore')
    header = form.querySelector('.modal-header')

    well = form.querySelector('select[name="well"]')
    well_id = well[well.selectedIndex].dataset.id


    wellbore = form.querySelector('input[name="wellbore"]')
    wellbore_name = wellbore.value
    wellbore_type_id = wellbore.dataset.id

    let is_gis = (form.querySelector('input[name="is_gis"]').checked) ? 1 : 0;
    let is_gti = (form.querySelector('input[name="is_gti"]').checked) ? 1 : 0;

    console.log(user_id)
    console.log(well_id)
    console.log(wellbore)
    console.log(wellbore_type_id)
    console.log(is_gis)
    console.log(is_gti)

    wellbore_type = form.querySelector('select[name="wellbore_type"]')
    wellbore_type_id = wellbore_type[wellbore_type.selectedIndex].dataset.id

    var formData = new FormData(document.forms.person);

    formData.append("user_id", user_id);
    formData.append("well_id", well_id);
    formData.append("name", wellbore_name);
    formData.append("wellbore_type_id", wellbore_type_id);
    formData.append("is_gis", is_gis);
    formData.append("is_gti", is_gti);

    var xhr = new XMLHttpRequest();
    url = 'http://' + document.location.host + '/api/wellbore'
    xhr.open("POST", url);
    xhr.send(formData);

    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            if(xhr.status == 200) {
                wellbores_div = document.getElementById('wellbores')
                wellbore = JSON.parse(xhr.responseText)

                header.innerHTML = 'Секция ' + wellbore['name'] + ' успешно добавлена'
            }
            if(xhr.status == 400 || xhr.status == 500) {
                header.innerHTML = 'Секция НЕ добавлена'
            }
        }
    }
}


function get_fields() {
    form = document.getElementById('add_wellbore')
    customer = form.querySelector('select[name="customer"]')
    customer_id = customer[customer.selectedIndex].dataset.id

    fields_opt = form.querySelector('select[name="field"]')
    pads_opt = form.querySelector('select[name="pad"]')
    wells_opt = form.querySelector('select[name="well"]')
    well_type = form.querySelector('input[name="well_type"]')
        // Удаление старых option
    fields_opt.length = 0;
    fields_opt.options[0] = new Option();
    pads_opt.length = 0;
    pads_opt.options[0] = new Option();
    wells_opt.length = 0;
    wells_opt.options[0] = new Option();
    well_type.value = ''

    xhr = new XMLHttpRequest();
    url = 'http://' + document.location.host + '/api/customer/' + customer_id
    xhr.open("GET", url);
    xhr.send();

    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            if(xhr.status == 200) {
                customer = JSON.parse(xhr.responseText)

                i = 1
                for (field of customer['fields']){
                    fields_opt.options[i] = new Option(field['name']);
                    fields_opt.options[i].setAttribute('data-id', field['id'])
                    i++
                }
            }
        }
    }
}

function get_pads() {
    form = document.getElementById('add_wellbore')
    field = form.querySelector('select[name="field"]')
    field_id = field[field.selectedIndex].dataset.id

    pads_opt = form.querySelector('select[name="pad"]')
    wells_opt = form.querySelector('select[name="well"]')
    well_type = form.querySelector('input[name="well_type"]')
    // Удаление старых option
    pads_opt.length = 0;
    pads_opt.options[0] = new Option();
    wells_opt.length = 0;
    wells_opt.options[0] = new Option();
    well_type.value = ''

    xhr = new XMLHttpRequest();
    url = 'http://' + document.location.host + '/api/field/' + field_id
    xhr.open("GET", url);
    xhr.send();

    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            if(xhr.status == 200) {
                field = JSON.parse(xhr.responseText)

                i = 1
                for (pad of field['pads']){
                    pads_opt.options[i] = new Option(pad['name']);
                    pads_opt.options[i].setAttribute('data-id', pad['id'])
                    i++
                }
            }
        }
    }
}

function get_wells() {
    form = document.getElementById('add_wellbore')
    pad = form.querySelector('select[name="pad"]')
    pad_id = pad[pad.selectedIndex].dataset.id

    wells_opt = form.querySelector('select[name="well"]')
    well_type = form.querySelector('input[name="well_type"]')
     // Удаление старых option
    wells_opt.length = 0;
    wells_opt.options[0] = new Option();
    well_type.value = ''

    xhr = new XMLHttpRequest();
    url = 'http://' + document.location.host + '/api/pad/' + pad_id
    xhr.open("GET", url);
    xhr.send();

    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            if(xhr.status == 200) {
                pad = JSON.parse(xhr.responseText)

                i = 1
                for (well of pad['wells']){
                    wells_opt.options[i] = new Option(well['name']);
                    wells_opt.options[i].setAttribute('data-id', well['id'])
                    wells_opt.options[i].setAttribute('data-type', well['well_type'])
                    wells_opt.options[i].setAttribute('onchange', 'set_well_type()')

                    i++
                }
            }
        }
    }
}

function set_well_type() {
    form = document.getElementById('add_wellbore')

    well = form.querySelector('select[name="well"]')
    well_type = form.querySelector('input[name="well_type"]')

    well_type.value = well[well.selectedIndex].dataset.type

}