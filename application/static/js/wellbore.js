function add_wellbore() {
    user = document.getElementById('user')
    user_id = user.dataset.id

    form = document.getElementById('add_wellbore')
    header = form.querySelector('.modal-header')

    well_id = form.querySelector('input[name="well"]').dataset.id

    wellbore = form.querySelector('input[name="wellbore"]').value

    let is_gis = (form.querySelector('input[name="is_gis"]').checked) ? 1 : 0;
    let is_gti = (form.querySelector('input[name="is_gti"]').checked) ? 1 : 0;

    wellbore_type_form = form.querySelector('select[name="wellbore_type"]')
    wellbore_type_index = wellbore_type_form.selectedIndex
    wellbore_type_id = wellbore_type_form[wellbore_type_index].dataset.id

    var formData = new FormData(document.forms.person);

    formData.append("user_id", user_id);
    formData.append("well_id", well_id);
    formData.append("wellbore", wellbore);
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

                console.log(wellbore)
                liFirst = document.createElement('li');
                liFirst.innerHTML = wellbore['name'] + ' ' + wellbore['wellbore_type']['name'];

                wellbores_div.prepend(liFirst)

                header.innerHTML = 'Секция ' + wellbore['name'] + ' успешно добавлена'
            }
            if(xhr.status == 400 || xhr.status == 500) {
                header.innerHTML = 'Секция НЕ добавлена'
            }
        }
    }
}
