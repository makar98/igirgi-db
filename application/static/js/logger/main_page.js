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
                log_div = $('#log')
                logs = JSON.parse(xhr.responseText)
                console.log(logs)
                console.log(log_div)
                while (log.firstChild) {
                    console.log()
                    log.removeChild(log.firstChild);
                }
                for (log of logs){
                    console.log(log)
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

                        field_div_col.innerHTML = field['__repr__'].split('<bound method EditableField.__repr__ of ')[1]

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