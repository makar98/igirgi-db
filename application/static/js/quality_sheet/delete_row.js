function delete_row(element) {
    // удаление строки из второй таблицы
    index = element.parentNode.parentNode.dataset.index;

    table_body_2 = document.getElementById('body_2')
    for (child of table_body_2.children){

        console.log(child.dataset.index)
        if (child.dataset.index==index){
            child.remove();
            console.log(child)
            break;
        }
    }

    // удаление строки из первой таблицы
    element.parentNode.parentNode.remove();
};