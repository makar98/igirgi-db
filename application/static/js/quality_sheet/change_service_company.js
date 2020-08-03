function change_service_company(element) {
    methods = document.getElementsByName('method')
    for (method of methods) {
        change_method(method)
    }
}

window.onload = function() {
    change_service_company()
}