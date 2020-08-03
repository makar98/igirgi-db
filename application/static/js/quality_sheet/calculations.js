setInterval(function() {
    las = get_las_value();
    info = get_information();
    rt_data = get_rt_data_value();

    tables_data = get_tables_value();

    rt_table = tables_data[0];
    no_data = tables_data[1];
    second_table = tables_data[2];
    document.getElementById('second_table_result').value = second_table
    result = rt_table * 0.1 + no_data * 0.1 + info * 0.2 + las * 0.1 + rt_data * 0.1 + second_table * 0.4;
    if (isNaN(result) === true) {
        document.getElementById('grade').value = 'Введены не все значения'
    }
    else {
        document.getElementById('grade').value = Math.round(result) + '%'
    }
}, 1000);

setInterval(function() {
    string_to_write = ''
    grade = 'Общая оценка качества каротажа составила: ' + document.getElementById('grade').value + '\n'
    string_to_write += grade
    if (grade!='100%'){
        string_to_write += 'Причиной применения понижающего коэффициента является: '
    }

    rt_coefficient_array = document.getElementsByName('rt_coefficient');
    rt_res = 0
    for (row of rt_coefficient_array){
        rt_res += Number.parseFloat(row.value)
    }
    rt_res = rt_res / rt_coefficient_array.length * 100
    if (rt_res < 100){
        string_to_write += 'низкая сходимость данных Real-time/Memory, '
    }

    no_data_coefficient_array = document.getElementsByName('no_data_coefficient');
    no_data_res = 0
    for (row of no_data_coefficient_array){
        no_data_res += Number.parseFloat(row.value)
    }
    no_data_res = no_data_res / rt_coefficient_array.length * 100
    if (no_data_res < 100){
        string_to_write += 'средний коэффициент отсутствия данных ' + Math.round(no_data_res) + '%, '
    }

    info = get_information();
    if (info !=100){
        string_to_write += 'передача и заполнение данных LQC не в полном объеме, '
    }
    las = get_las_value();
    if (las !=100){
        string_to_write += 'некорректное оформление las файла, '
    }
    rt_data = get_rt_data_value();
    if (rt_data !=100){
        string_to_write += 'некорректное настройка дынных Real-time, '
    }

    linkage_by_depth_array = document.getElementsByName('linkage_by_depth');
    linkage_by_depth_string = ''
    for (row of linkage_by_depth_array){
        if (row.value === 'Частично неувязан'){
            linkage_by_depth_string = 'частичная неувязка по глубине, '
        }
        else if (row.value === 'Неувязан'){
            linkage_by_depth_string = 'неувязка данных по глубине, '
            break;
        }
    }
    string_to_write += linkage_by_depth_string

    emissions_array = document.getElementsByName('emissions');
    emissions_string = ''
    for (row of emissions_array){
        if (row.value === 'Единичные'){
            emissions_string = 'единичные выбросы в данных из памяти прибора, '
        }
        else if (row.value === 'Регулярные'){
            emissions_string = 'наличие выбросов в данных из памяти прибора, '
            break;
        }
    }
    string_to_write += emissions_string

    noise_array = document.getElementsByName('noise');
    noise_string = ''
    for (row of noise_array){
        if (row.value === 'Незначительная'){
            noise_string = 'единичные выбросы в данных из памяти прибора, '
        }
        else if (row.value === 'Выше допустимой'){
            noise_string = 'наличие выбросов в данных из памяти прибора, '
            break;
        }
    }
    string_to_write += noise_string

    check_measurement_array = document.getElementsByName('check_measurement');
    check_measurement_string = ''
    for (row of check_measurement_array){
        if (row.value === 'Не соответствует основному замеру'){
            check_measurement_string = 'повторный замер не соответствует основной записи, '
            break;
        }
        else if (row.value === 'Не произведен'){
            check_measurement_string = 'отсутствие повторных замеров, '
            break;
        }
    }
    string_to_write += check_measurement_string

    cross_plot_distribution_array = document.getElementsByName('cross_plot_distribution');
    cross_plot_distribution_string = ''
    for (row of cross_plot_distribution_array){
        if (row.value === 'Занижены'){
            cross_plot_distribution_string = 'занижение значений на кросс-плоте, '
        }
        else if (row.value === 'Завышены'){
            cross_plot_distribution_string = 'завышение значений на кросс-плоте, '
        }
        else if (row.value === 'Не соответствуют'){
            cross_plot_distribution_string = 'не соответствие значений на кросс-плоте, '
            break;
        }
    }
    string_to_write += cross_plot_distribution_string

    tool_indication_array = document.getElementsByName('tool_indication');
    tool_indication_string = ''
    for (row of tool_indication_array){
        if (row.value === 'Занижены'){
            tool_indication_string = 'занижение показаний прибора в исследуемом разрезе, '
        }
        else if (row.value === 'Завышены'){
            tool_indication_string = 'завышение показаний прибора в исследуемом разрезе '
        }
        else if (row.value === 'Не соответствуют'){
            tool_indication_string = 'не соответствие показаний прибора в исследуемом разрезе, '
            break;
        }
    }
    string_to_write += tool_indication_string

    absolute_petrophysical_values_array = document.getElementsByName('absolute_petrophysical_values');
    absolute_petrophysical_values_string = ''
    for (row of absolute_petrophysical_values_array){
        if (row.value === 'Занижены'){
            absolute_petrophysical_values_string = 'занижение значений в опорных пластах, '
        }
        else if (row.value === 'Завышены'){
            absolute_petrophysical_values_string = 'завышение значений в опорных пластах, '
        }
        else if (row.value === 'Не соответствуют'){
            absolute_petrophysical_values_string = 'не соответствие значений в опорных пластах, '
            break;
        }
    }
    string_to_write += absolute_petrophysical_values_string
    document.getElementById('result_comment').innerHTML = string_to_write
}, 1000);

function get_information() {
    values = []
    title_page = document.getElementsByName('title_page')[0].value;
    values.push(title_page)

    construct = document.getElementsByName('construct')[0].value;
    values.push(construct)

    column_size = document.getElementsByName('column_size')[0].value;
    values.push(column_size)

    well_chronology = document.getElementsByName('well_chronology')[0].value;
    values.push(well_chronology)

    drilling_fluid_info = document.getElementsByName('drilling_fluid_info')[0].value;
    values.push(drilling_fluid_info)

    tool_composition = document.getElementsByName('tool_composition')[0].value;
    values.push(tool_composition)

    depth_control_data = document.getElementsByName('depth_control_data')[0].value;
    values.push(depth_control_data)

    directional_survey_data = document.getElementsByName('directional_survey_data')[0].value;
    values.push(directional_survey_data)

    main_record = document.getElementsByName('main_record')[0].value;
    values.push(main_record)

    data_processing_and_tool_parameters = document.getElementsByName('data_processing_and_tool_parameters')[0].value;
    values.push(data_processing_and_tool_parameters)

    second_record = document.getElementsByName('second_record')[0].value;
    values.push(second_record)

    curve_control_pad = document.getElementsByName('curve_control_pad')[0].value;
    values.push(curve_control_pad)

    tool_calibration = document.getElementsByName('tool_calibration')[0].value;
    values.push(tool_calibration)

    let las_val_sum
    las_val_sum = 0;
    let coef
    for (val of values) {
    if (val === 'Полная') {
        coef = 1
    }
    if (val === 'Частичная') {
        coef = 0.5
    }
    if (val === 'Отстутсвует') {
        coef = 0
    }
    las_val_sum = las_val_sum + coef
    }
    document.getElementById('information').value = Math.round(las_val_sum / 13 * 100) + '%'
    return Math.round(las_val_sum / 13 * 100)
    }

    function get_las_value() {
    values = []
    well = document.getElementsByName('las_file_design_well_section')[0].value;
    values.push(well)
    parameters = document.getElementsByName('las_file_design_parameters_section')[0].value;
    values.push(parameters)
    curve = document.getElementsByName('las_file_design_curve_section')[0].value;
    values.push(curve)
    let las_val_sum
    las_val_sum = 0;
    let coef
    for (val of values) {
        if (val === 'Полная') {
            coef = 1
        }
        if (val === 'Частичная') {
            coef = 0.5
        }
        if (val === 'Отстутсвует') {
            coef = 0
        }
        las_val_sum = las_val_sum + coef
        }

        document.getElementById('las_file_design').value = Math.round(las_val_sum / 3 * 100) + '%'
        return Math.round(las_val_sum / 3 * 100)
    }

    function get_rt_data_value() {
    values = []
    data_completeness = document.getElementsByName('data_completeness')[0].value;
    values.push(data_completeness)

    data_transfer_settings = document.getElementsByName('data_transfer_settings')[0].value;
    values.push(data_transfer_settings)

    curve_names = document.getElementsByName('curve_names')[0].value;
    values.push(curve_names)

    mnemonic_description = document.getElementsByName('mnemonic_description')[0].value;
    values.push(mnemonic_description)

    let las_val_sum
    las_val_sum = 0;
    let coef
    for (val of values) {
    if (val === 'Полная') {
        coef = 1
    }
    if (val === 'Частичная') {
        coef = 0.5
    }
    if (val === 'Отстутсвует') {
        coef = 0
    }
    las_val_sum = las_val_sum + coef
    }
    document.getElementById('incorrect_RT_data').value = Math.round(las_val_sum / 4 * 100) + '%'
    return Math.round(las_val_sum / 4 * 100)
    }


function get_tables_value() {
    values = []
    rt_coefficient_array = document.getElementsByName('rt_coefficient');

    no_data_coefficient_array = document.getElementsByName('no_data_coefficient');

    linkage_by_depth_array = document.getElementsByName('linkage_by_depth');

    emissions_array = document.getElementsByName('emissions');

    noise_array = document.getElementsByName('noise');

    check_measurement_array = document.getElementsByName('check_measurement');

    cross_plot_distribution_array = document.getElementsByName('cross_plot_distribution');

    tool_indication_array = document.getElementsByName('tool_indication');

    absolute_petrophysical_values_array = document.getElementsByName('absolute_petrophysical_values');

    let rt_coefficient_value
    rt_coefficient_value = 0

    let no_data_coefficient_value
    no_data_coefficient_value = 0

    let second_table_value
    second_table_value = 0

    for (let i=0; i < rt_coefficient_array.length; i++) {
    rt_coefficient_value = rt_coefficient_value + Number.parseFloat(rt_coefficient_array[i].value);
    no_data_coefficient_value = no_data_coefficient_value + Number.parseFloat(no_data_coefficient_array[i].value);

    second_table_row_values = []
    second_table_row_values.push(linkage_by_depth_array[i].value)
    second_table_row_values.push(emissions_array[i].value)
    second_table_row_values.push(noise_array[i].value)
    second_table_row_values.push(check_measurement_array[i].value)
    second_table_row_values.push(cross_plot_distribution_array[i].value)
    second_table_row_values.push(tool_indication_array[i].value)
    second_table_row_values.push(absolute_petrophysical_values_array[i].value)

    let second_table_row_value
    second_table_row_value = 0
    for (val of second_table_row_values) {
        if (val === 'Увязан' || val === 'Отсутствуют' || val === 'Отсутствует' ||
            val === 'Соответствует основному замеру' ||
            val === 'Отменен по согласованию сторон' ||
            val === 'Опорные пласты не вскрыты' ||
            val === 'Произведен' || val === 'Соответствуют') {
            coef = 1
        }
        else if (val === 'Частично неувязан' ||val === 'Единичные' || val === 'Незначительная' ||
            val === 'Занижены' || val === 'Завышены') {
            coef = 0.5
        }
        else if (val === 'Неувязан' || val === 'Регулярные' || val === 'Выше допустимой' ||
            val === 'Не соответствует основному замеру' ||
            val === 'Не произведен' || val === 'Не соответствуют') {
            coef = 0
        }
        else {
            coef = NaN
        }
        second_table_row_value = second_table_row_value + coef

    }
    second_table_value = second_table_value + second_table_row_value / 7
    }
    result = []
    result.push(Math.round(rt_coefficient_value / rt_coefficient_array.length * 100))
    result.push(Math.round(no_data_coefficient_value / rt_coefficient_array.length * 100))
    result.push(Math.round(second_table_value / rt_coefficient_array.length * 100))
    return result
}