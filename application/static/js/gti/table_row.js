function edit_row(elem) {
    check = confirm('Сохранить изменения в БД?');
    if (!check){
        return
        }

    form = elem.parentNode.parentNode

    table_row_id = elem.dataset.table_row_id

    header = form.querySelector('.modal-header')

    modal_id = form.parentNode.parentNode.parentNode.id

    quality_selector = "#quality_" + modal_id
    wellbore_status_selector = "#wellbore_status_" + modal_id
    final_report_selector = "#final_report_" + modal_id
    service_company_selector = "#service_company_" + modal_id
    station_type_selector = "#station_type_" + modal_id
    degasser_type_selector = "#degasser_type_" + modal_id
    chromatograph_type_selector = "#chromatograph_type_" + modal_id
    layers_selector = "#layers_" + modal_id

    console.log(layers_selector)

    var quality_id = $(quality_selector).val()
    var wellbore_status_id = $(wellbore_status_selector).val()
    var final_report_id = $(final_report_selector).val()
    var service_company_id = $(service_company_selector).val()
    var station_type_id = $(station_type_selector).val()
    var degasser_type_id = $(degasser_type_selector).val()
    var chromatograph_type_id = $(chromatograph_type_selector).val()
    var layers_id = $(layers_selector).val()

    date_T3 = form.querySelector('input[name="date_T3"]').value
    factory_num = form.querySelector('input[name="factory_num"]').value
    frequency = form.querySelector('input[name="frequency"]').value
    notes = form.querySelector('textarea[name="notes"]').value

    var formData = new FormData(document.forms.person);
    if (typeof quality_id != "undefined" & quality_id != null & quality_id != ''){
        formData.append("quality_id", quality_id);
    }
    if (typeof wellbore_status_id != "undefined" & wellbore_status_id != null & wellbore_status_id != ''){
        formData.append("wellbore_status_id", wellbore_status_id);
    }
    if (typeof final_report_id != "undefined" & final_report_id != null & final_report_id != ''){
        formData.append("final_report_id", final_report_id);
    }
    if (typeof service_company_id != "undefined" & service_company_id != null & service_company_id != ''){
        formData.append("service_company_id", service_company_id);
    }
    if (typeof station_type_id != "undefined" & station_type_id != null & station_type_id != ''){
        formData.append("station_type_id", station_type_id);
    }
    if (typeof degasser_type_id != "undefined" & degasser_type_id != null & degasser_type_id != ''){
        formData.append("degasser_type_id", degasser_type_id);
    }
    if (typeof chromatograph_type_id != "undefined" & chromatograph_type_id != null & chromatograph_type_id != ''){
        formData.append("chromatograph_type_id", chromatograph_type_id);
    }
    if (typeof date_T3 != "undefined" & date_T3 != null & date_T3 != ''){
        formData.append("date_T3", date_T3);
    }
    if (typeof frequency != "undefined" & frequency != null & frequency != ''){
        formData.append("frequency", frequency);
    }
    if (typeof factory_num != "undefined" & factory_num != null & factory_num != ''){
        formData.append("factory_num", factory_num);
    }
    if (typeof notes != "undefined" & notes != null & notes != ''){
        formData.append("notes", notes);
    }
    console.log(layers_id)
    if (typeof layers_id != "undefined" & layers_id != null & layers_id != ''){
        formData.append("layers_id", JSON.stringify(layers_id));
    }

    var xhr = new XMLHttpRequest();
    url = 'http://' + document.location.host + '/api/gti/table_row/' + table_row_id
    xhr.open("PUT", url);
    xhr.send(formData);

    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            if(xhr.status == 201) {
                response = JSON.parse(xhr.responseText)
                //header.innerHTML = 'Успех'
            }
            if(xhr.status == 400 || xhr.status == 500) {
                //header.innerHTML = 'Провал'
            }
        }
    }
}


function get_rows_filter() {
    search = $('#search .selectpicker')

    search_validate = false

    search.each(function( index ) {
        if ($( this ).val()){

        }
        else{
            search_validate = true // наверное, тру и фолс нужно поменять местами
        }
    });

    if (search_validate){
        alert('Ошибка! Убедитесь, что введены все значения')
        return
    }

    param_obj = {}

    param_obj['users'] = $('#users_search').val()

    param_obj['date_interval'] = $('#date_interval_search').val()
    param_obj['sort'] = $('#sort_search').val()

    param_obj['fields'] = $('#fields_search').val()
    param_obj['layers'] = $('#layers_search').val()
    param_obj['customers'] = $('#customers_search').val()
    param_obj['service_companies'] = $('#gti_service_companies_search').val()
    param_obj['wellbore_statuses'] = $('#wellbore_statuses_search').val()
    param_obj['qualities'] = $('#quality_search').val()

    console.log(param_obj['gti_service_companies'])

    validators = [null, 'null', '', ' ', undefined, 'undefined']
    param = '?filter=true&'
    for (key in param_obj){
        if (validators.includes(param_obj[key])){

        }
        else{
            if (param == '?filter=true&'){
                param = param + key + '=' + param_obj[key]
            }
            else{
                param = param + '&' + key + '=' + param_obj[key]
            }
        }
    }

    var xhr = new XMLHttpRequest();
    //param = ('?users=' + users + '&date_interval=' + date_interval +
        //    '&customers=' + customers + '&gti_service_companies=' + gti_service_companies +
         //   '&wellbore_statuses=' + wellbore_statuses + '&quality=' + quality
         //   )
    console.log(param)
    url = 'http://' + document.location.host + '/gti/tbl' + param
    window.location.replace(url);
    /*
    xhr.open("GET", url);
    xhr.send();
    main_data_rows = $('#main_data_rows')

    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            if(xhr.status == 200) {
                //console.log('eeee')
                main_data_rows_div = $('#main_data_rows')
                main_data_rows = $('#main_data_rows > div')
                main_data_rows.each( function( index, element) {
                    //console.log(element);
                });

                rows = JSON.parse(xhr.responseText)
                for (row of rows){
                    console.log(row)
                }

            }
            if(xhr.status == 400 || xhr.status == 500) {
                alert('Ошибка! Пока непонятная')
            }
        }
    }
    */
}
