function change_method(element) {

    service_company_select = document.getElementById('service_company')

    service_company = service_company_select.options[service_company_select.selectedIndex]

    service_company_id = service_company.dataset.id

    method = element.value

    // Редактирование второй таблицы
    index = element.parentNode.parentNode.dataset.index;
    table_body_2 = document.getElementById('body_2')
    for (child of table_body_2.children){
        if (child.dataset.index==index){
            child.children[0].innerHTML = '<span>' + method + '</span>'
            break;
        }
    }

    var xhr = new XMLHttpRequest();
    var url = 'http://' + document.location.host + '/api/service_company/' + service_company_id
    xhr.open('GET', url)
    xhr.setRequestHeader("Content-Type", "application/json");
    let tools = [];
    xhr.send()
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            data = JSON.parse(xhr.responseText)
            for (tool of data['tools']) {
                if (tool['tool_type']==method){
                    tools.push(tool)
                }
            }
            opt = document.createElement('select');
            opt.setAttribute("name", "tool_type");

            j = 0
            console.log(tools)
            if (tools.length != 0) {
                for (tool of tools) {
                    opt.options[j] = new Option(tool['name']);
                    opt.options[j].dataset.id=tool['id'];
                    j++;
                }
            }
            else {
                opt.options[0] = new Option();
            }

            tools_old = element.parentNode.parentNode.children[1].children[0].children[0].children[0]
            parent_node = tools_old.parentNode
            parent_node.replaceChild(opt, tools_old);
        }
    }
}