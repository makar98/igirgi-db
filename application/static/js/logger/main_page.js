function get_log() {
    users = $('#users').val()
    date_interval = $('#date_interval').val()
    sort = $('#sort').val()

    var xhr = new XMLHttpRequest();
    param = '?users=' + users + '&date_interval=' + date_interval + '&sort=' + sort
    url = 'http://' + document.location.host + '/api/logger' + param
    xhr.open("GET", url);
    xhr.send();

    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) {
            if(xhr.status == 200) {
                log_div = $('#log')[0]
                //console.log(logs)
                console.log(log_div)
                console.log(log_div.children)
                while (log_div.firstChild) {
                    //console.log(log_div.firstChild)
                    log_div.removeChild(log_div.firstChild);
                }

                logs = JSON.parse(xhr.responseText)
                for (log of logs){
                    //console.log(log)
                    div_row = document.createElement('div');
                    div_row.classList.add('row')
                    div_row.setAttribute('style', 'background-color: #fa9d10;')

                    div_col = document.createElement('div');
                    div_col.classList.add('col')
                    div_col.innerHTML = '#' + log['id']

                    div_row.append(div_col)
                    log_div.append(div_row)

                    for (field of log['editable_fields']){
                        field_div_row = document.createElement('div');
                        field_div_row.classList.add('row')

                        field_div_col = document.createElement('div');
                        field_div_col.classList.add('col')

                        data = field['__repr__'].split('<bound method EditableField.__repr__ of ')[1]
                        data = data.substring(0, data.length - 1)

                        field_div_col.innerHTML = data

                        field_div_row.append(field_div_col)
                        log_div.append(field_div_row)
                    }

                }
            }
            if(xhr.status == 400 || xhr.status == 500) {

            }
        }
    }
}