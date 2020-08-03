function get_tool(service_company_id, method) {
    var xhr = new XMLHttpRequest();
    var url = 'http://' + document.location.host + '/api/service_company/' + service_company_id
    xhr.open('GET', url)
    xhr.setRequestHeader("Content-Type", "application/json");
    let result = [];
    let result_length = -1;
    xhr.send()
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            data = JSON.parse(xhr.responseText)
            for (tool of data['tools']){
                if (tool['tool_type']==method){
                    result_length += 1
                    result[result_length] = tool
                }
            }

        }
    }
    return result
}
