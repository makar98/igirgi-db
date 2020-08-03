function get_fields_list(customer_obj) {
    var customer = customer_obj.value;
    var xhr = new XMLHttpRequest();

    var url = 'http://' + document.location.host + '/get_fields_json/' + customer;
    xhr.open('POST', url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send();
    //xhr.send(customer);
    elements = customer_obj.parentNode.parentNode.parentNode.elements
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            if(xhr.status == 200) {
                fields = JSON.parse(xhr.responseText)
                opt = elements['field']
                // Удаление старых option
                opt.length = 0;
                opt.options[0] = new Option();
                i = 1
                for (field of fields){
                    opt.options[i] = new Option(field);
                    i++
                }
            }
            else{
                elements['field'].length = 0;
            }
        }
    };
    elements['pad'].length = 0;
}

function get_pads_list(field_obj) {
    var field = field_obj.value;
    var xhr = new XMLHttpRequest();

    var url = 'http://' + document.location.host + '/get_pads_json/' + field;
    xhr.open('POST', url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send();
    elements = field_obj.parentNode.parentNode.parentNode.elements
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            if(xhr.status == 200) {
                pads = JSON.parse(xhr.responseText)
                opt = elements['pad'];
                // Удаление старых option
                opt.length = 0;
                opt.options[0] = new Option();
                i = 1
                for (pad of pads){
                    opt.options[i] = new Option(pad);
                    i++
                }
            }
            else{
                elements['pad'].length = 0;
            }
        }
    };
}

function get_wells_list(pad_obj) {
    var pad = pad_obj.value;
    var xhr = new XMLHttpRequest();

    var url = 'http://' + document.location.host + '/get_wells_json/' + pad;
    xhr.open('POST', url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send()
    elements = pad_obj.parentNode.parentNode.parentNode.elements
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            if(xhr.status == 200) {
                wells = JSON.parse(xhr.responseText)
                opt = elements['well'];
                // Удаление старых option
                opt.length = 0;
                opt.options[0] = new Option();
                i = 1
                for (well of wells){
                    opt.options[i] = new Option(well);
                    i++
                }

            }
        }
    };
}

function get_wellbores_list(well) {
    var well = well.value;
    var xhr = new XMLHttpRequest();

    var url = 'http://' + document.location.host + '/get_wellbores_json/' + well;
    xhr.open('POST', url, true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send()
    xhr.onreadystatechange = function() {
    if (xhr.readyState == 4) {
        if(xhr.status == 200) {
            wellbores = JSON.parse(xhr.responseText)
            opt = document.getElementById('wellbore');
            // Удаление старых option
            opt.length = 0;
            opt.options[0] = new Option();
            i = 1
            for (wellbore of wellbores){
                opt.options[i] = new Option(wellbore);
                i++
            }
            var to_replace = document.getElementById('wellbore')
            var parentDiv = to_replace.parentNode;
            parentDiv.replaceChild(opt, to_replace);
            }
        }
    };
}