from application import app
from flask import render_template, request, url_for, redirect
import json
from application.models.models import Customer, Field, ServiceCompany, Tool
from application import db


@app.route('/', methods=['post', 'get'])
def index():
    if request.method == 'POST':
        """
        data from techlog
        dict_prop = request.values
       # for key, val in dict_prop.items():
            #print('{}: {}'.format(key, val))
            #print(key)
        dict_prop = dict(dict_prop)
        for k, v in dict_prop.items():
            print('{}: {}'.format(k, v))
        #print(dict_prop['MST'])

        req_js = request.get_json()
        for key, val in req_js.items():
            #print('{}: {}'.format(key, val))
            print(key)
            for k, v in val.items():
                print('{}: {}'.format(k, v))
       """
        #return render_template('test.html', Company='TL_ServerWellID')
        pass
    customers = Customer.query.all()
    companies = ServiceCompany.query.all()

    return render_template('edit_page.html', data=request.args, customers=customers, companies=companies)


@app.route('/customers')
def customers():
    customers_list = Customer.query.all()
    return render_template('customer_list.html', customers_list=customers_list)


@app.route('/companies')
def companies():
    companies_list = ServiceCompany.query.all()
    return render_template('companies_list.html', companies_list=companies_list)


@app.route('/add_customer', methods=['post', 'get'])
def add_customer():
    if request.method == 'POST':
        customer_name = request.form.get('customer_to_add')
        customer_to_add = Customer(name=customer_name)
        db.session.add(customer_to_add)
        db.session.commit()
    return redirect(url_for('customers'))


@app.route('/add_company', methods=['post', 'get'])
def add_company():
    if request.method == 'POST':
        company_name = request.form.get('company_to_add')
        company_to_add = ServiceCompany(name=company_name)
        db.session.add(company_to_add)
        db.session.commit()
    return redirect(url_for('companies'))


@app.route('/delete_customer/<customer_name>', methods=['post', 'get'])
def delete_customer(customer_name):
    if request.method == 'POST':
        # либо удалять не первый элемент, лиюо customer_name.unique = True
        customer_to_del = db.session.query(Customer).filter_by(name=customer_name).first()
        for field in customer_to_del.fields:
            db.session.delete(field)
        db.session.delete(customer_to_del)
        db.session.commit()
        return redirect(url_for('customers'))


@app.route('/delete_company/<company_name>', methods=['post', 'get'])
def delete_company(company_name):
    if request.method == 'POST':
        company_to_del = db.session.query(ServiceCompany).filter_by(name=company_name).first()
        for tool in company_to_del.tools:
            db.session.delete(tool)
        db.session.delete(company_to_del)
        db.session.commit()
        return redirect(url_for('companies'))


@app.route('/customer/<customer_name>')
def customer(customer_name):
    customer = Customer.query.filter_by(name=customer_name).first_or_404()
    fields = customer.fields
    return render_template('add_field.html', customer=customer, fields=fields)


@app.route('/company/<company_name>')
def company(company_name):
    company = ServiceCompany.query.filter_by(name=company_name).first_or_404()
    tools = company.tools

    # electric
    lateral_log = []
    lateral_microlog = []
    induction_log = []
    vikiz = []
    attenuation_log = []
    lateral_image = []

    # radio
    integrated_gr = []
    spectrometric_gr = []
    neutron_log = []
    pulse_neutron_log = []
    oxy_carbon_log = []
    density_ggr = []
    density_lito_ggr = []
    photoelectric_image_ggr = []

    # acoustic
    refracted_acoustic_log = []
    reflected_acoustic_log = []

    # cali
    mechanical_caliper = []
    density_caliper = []
    acoustic_caliper = []

    # cmr
    cmr = []

    for tool in tools:
        if tool.tool_type == 'Боковой каротаж':
            lateral_log.append(tool.name)
        elif tool.tool_type == 'Боковой микрокаротаж':
            lateral_microlog.append(tool.name)
        elif tool.tool_type == 'Индукционный каротаж':
            induction_log.append(tool.name)
        elif tool.tool_type == 'Высокочастотное индукционное каротажное изопараметрическое зондирование':
            vikiz.append(tool.name)
        elif tool.tool_type == 'Электромагнитный каротаж по затуханию':
            attenuation_log.append(tool.name)
        elif tool.tool_type == 'Азимутальный электрический микроимиджер':
            lateral_image.append(tool.name)

        elif tool.tool_type == 'Интегральный гамма-каротаж':
            integrated_gr.append(tool.name)
        elif tool.tool_type == 'Спектрометрический гамма-каротаж':
            spectrometric_gr.append(tool.name)
        elif tool.tool_type == 'Нейтронный каротаж':
            neutron_log.append(tool.name)
        elif tool.tool_type == 'Импульсный нейтронный каротаж':
            pulse_neutron_log.append(tool.name)
        elif tool.tool_type == 'Импульсный спектрометрический нейтронный гамма-каротаж':
            oxy_carbon_log.append(tool.name)
        elif tool.tool_type == 'Гамма-гамма плотностной':
            density_ggr.append(tool.name)
        elif tool.tool_type == 'Гамма-гамма литоплотностной каротаж (Объемная плотность)':
            density_lito_ggr.append(tool.name)
        elif tool.tool_type == 'Гамма-гамма литоплотностной каротаж (Индекс фотоэлектрического поглощения)':
            photoelectric_image_ggr.append(tool.name)

        elif tool.tool_type == 'Акустический каротаж на преломленных волнах':
            refracted_acoustic_log.append(tool.name)
        elif tool.tool_type == 'Акустический каротаж па отраженных волнах':
            reflected_acoustic_log.append(tool.name)

        elif tool.tool_type == 'Каверномер':
            mechanical_caliper.append(tool.name)
        elif tool.tool_type == 'Плотностной каверномер':
            density_caliper.append(tool.name)
        elif tool.tool_type == 'Акустический каверномер':
            acoustic_caliper.append(tool.name)

        elif tool.tool_type == 'Ядерно-магнитный каротаж в сильном поле':
            cmr.append(tool.name)

    return render_template('add_tool.html', company=company, tools=tools,
                           lateral_log=lateral_log, lateral_microlog=lateral_microlog, induction_log=induction_log,
                           vikiz=vikiz, attenuation_log=attenuation_log, lateral_image=lateral_image,
                           integrated_gr=integrated_gr, spectrometric_gr=spectrometric_gr,
                           neutron_log=neutron_log, pulse_neutron_log=pulse_neutron_log, oxy_carbon_log=oxy_carbon_log,
                           density_ggr=density_ggr, density_lito_ggr=density_lito_ggr,
                           photoelectric_image_ggr=photoelectric_image_ggr,
                           refracted_acoustic_log=refracted_acoustic_log, reflected_acoustic_log=reflected_acoustic_log,
                           mechanical_caliper=mechanical_caliper, density_caliper=density_caliper,
                           acoustic_caliper=acoustic_caliper, cmr=cmr)


@app.route('/add_field', methods=['post', 'get'])
def add_field():
    if request.method == 'POST':
        field_name = request.form.get('field_to_add')
        customer_name = request.form.get('customer')
        customer = db.session.query(Customer).filter_by(name=customer_name).first()
        field_to_add = Field(name=field_name, customer=customer)
        db.session.add(field_to_add)
        db.session.commit()
        return redirect(url_for('customer', customer_name=customer_name))


@app.route('/add_tool', methods=['post', 'get'])
def add_tool():
    if request.method == 'POST':
        tool_name = request.form.get('tool_to_add')
        company_name = request.form.get('company')
        company = db.session.query(ServiceCompany).filter_by(name=company_name).first()
        selected_method = request.form.get('method')
        print(selected_method)
        tool_to_add = Tool(name=tool_name, ServiceCompany=company, tool_type=selected_method)
        db.session.add(tool_to_add)
        db.session.commit()
        return redirect(url_for('company', company_name=company_name))


@app.route('/delete_field/<field_name>', methods=['post', 'get'])
def delete_field(field_name):
    if request.method == 'POST':
        customer_name = request.form.get('customer')
        # либо удалять не первый элемент, лиюо field_name.unique = True
        field_to_del = db.session.query(Field).filter_by(name=field_name).first()
        db.session.delete(field_to_del)
        db.session.commit()
        customers_list = Customer.query.all()
        return redirect(url_for('customer', customer_name=customer_name))


@app.route('/delete_tool/<tool_name>', methods=['post', 'get'])
def delete_tool(tool_name):
    if request.method == 'POST':
        company_name = request.form.get('company')
        # либо удалять не первый элемент, лиюо field_name.unique = True
        tool_to_del = db.session.query(Tool).filter_by(name=tool_name).first()
        db.session.delete(tool_to_del)
        db.session.commit()
        customers_list = Customer.query.all()
        return redirect(url_for('company', company_name=company_name))


@app.route('/get_customer_json/<customer>', methods=['GET', 'POST'])
def get_customer_json(customer):
    fields = db.session.query(Customer).filter_by(name=customer).first().fields
    fields_list = []
    for f in fields:
        fields_list.append(str(f))
    return json.dumps(fields_list)


@app.route('/get_tool_json/<company>', methods=['GET', 'POST'])
def get_tool_json(company):
    tools = db.session.query(ServiceCompany).filter_by(name=company).first().tools
    tool_list = {}
    for t in tools:
        tool_list[str(t)] = t.tool_type
    return json.dumps(tool_list)


@app.route('/save_to_db', methods=['post', 'get'])
def save_to_db():
    if request.method == 'POST':
        customer = request.form.get('customer').strip()
        field = request.form.get('field').strip()
        pad_num = request.form.get('pad_num').strip()
        well_num = request.form.get('well_num').strip()
        service_company = request.form.get('service_company').strip()
        well_section = request.form.get('well_section').strip()
        section_interval_beg = request.form.get('section_interval_beg').strip()
        section_interval_end = request.form.get('section_interval_end').strip()
        section_diameter = request.form.get('section_diameter').strip()

        information = request.form.get('information').strip()
        title_page = request.form.get('title_page').strip()
        construct = request.form.get('construct').strip()
        column_size = request.form.get('column_size').strip()
        well_chronology = request.form.get('well_chronology').strip()
        drilling_fluid_info = request.form.get('drilling_fluid_info').strip()
        tool_composition = request.form.get('tool_composition').strip()
        depth_control_data = request.form.get('depth_control_data').strip()
        directional_survey_data = request.form.get('directional_survey_data').strip()
        main_record = request.form.get('main_record').strip()
        data_processing_and_tool_parameters = request.form.get('data_processing_and_tool_parameters').strip()
        second_record = request.form.get('second_record').strip()
        curve_control_pad = request.form.get('curve_control_pad').strip()
        tool_calibration = request.form.get('tool_calibration').strip()

        las_file_design = request.form.get('las_file_design').strip()
        las_file_design_well_section = request.form.get('las_file_design_well_section').strip()
        las_file_design_parameters_section = request.form.get('las_file_design_parameters_section').strip()
        las_file_design_curve_section = request.form.get('las_file_design_curve_section').strip()

        incorrect_RT_data = request.form.get('incorrect_RT_data').strip()
        data_completeness = request.form.get('data_completeness').strip()
        data_transfer_settings = request.form.get('data_transfer_settings').strip()
        curve_names = request.form.get('curve_names').strip()
        mnemonic_description = request.form.get('mnemonic_description').strip()

        linkage_by_depth = request.form.get('linkage_by_depth').strip() #  AttributeError: 'NoneType'
                                                                        # object has no attribute 'strip'
        emissions = request.form.get('emissions').strip()
        noise = request.form.get('noise').strip()
        check_measurement = request.form.get('check_measurement').strip()
        cross_plot_distribution = request.form.get('cross_plot_distribution').strip()
        tool_indication = request.form.get('tool_indication').strip()
        absolute_petrophysical_values = request.form.get('absolute_petrophysical_values').strip()
        notes = request.form.get('notes').strip()
        grade = request.form.get('grade').strip()

        # Это нужно сделать плосле добавления записи CL в БД, чтобы сделать связь methods --> CL
        method_row_len = len(request.form.getlist('method'))
        for row in range(method_row_len):
            method = request.form.get('method')
            tool_type = request.form.get('tool_type')
            tool_num = request.form.get('tool_num')
            calibration_date = request.form.get('calibration_date')
            gis_date = request.form.get('gis_date')
            receipt_date = request.form.get('receipt_date')
            interval_beg = request.form.get('interval_beg')
            interval_end = request.form.get('interval_end')
            rt_coefficient = request.form.get('rt_coefficient')
            no_data_coefficient = request.form.get('no_data_coefficient')


        return redirect('/')
        """
        customer
        field
        pad_num
        well_num
        service_company
        well_section
        section_interval_beg
        section_interval_end
        section_diameter
    
        method
        tool_type
        tool_num
        calibration_date
        gis_date
        receipt_date
        interval_beg
        interval_end
        rt_coefficient
        no_data_coefficient
    
        information
        title_page
        construct
        column_size
        well_chronology
        drilling_fluid_info
        tool_composition
        depth_control_data
        directional_survey_data
        main_record
        data_processing_and_tool_parameters
        second_record
        curve_control_pad
        tool_calibration
    
        las_file_design
        las_file_design_well_section
        las_file_design_parameters_section
        las_file_design_curve_section
    
        incorrect_RT_data
        data_completeness
        data_transfer_settings
        curve_names
        mnemonic_description
    
        -
        linkage_by_depth
        emissions
        noise
        check_measurement
        cross_plot_distribution
        tool_indication
        absolute_petrophysical_values
        notes
        grade
        """




