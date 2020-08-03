from application import app
from flask import render_template, request, url_for, redirect, make_response, jsonify

from sqlalchemy.exc import IntegrityError
from sqlalchemy import asc, desc

import json

from application.models.models import ServiceCompany
from application.models.models import Customer
from application.models.models import Field
from application.models.models import Pad
from application.models.models import Layer
from application.models.models import Well
from application.models.models import WellType
from application.models.models import Wellbore
from application.models.models import WellboreType
from application.models.models import QualitySheet
from application.models.models import GisCurve
from application.models.models import GisCurveCategory
from application.models.logger import Logger

from application import db
import os
from flask_security import login_required, logout_user, roles_required


@app.route('/')
def index():
    return redirect(url_for('new_style_index'))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/new_style_index', methods=['GET', 'POST'])
@login_required
def new_style_index():
    return render_template(r'new_style_base.html')


@app.route('/db', methods=['GET', 'POST'])
@login_required
@roles_required('test_role')
def db_page():
    return render_template(r'database.html')


@app.route('/gis', methods=['GET', 'POST'])
@login_required
@roles_required('test_role')
def gis():
    return render_template(r'gis/gis_main_page.html')


@app.route('/gis/curves', methods=['GET', 'POST'])
@login_required
@roles_required('test_role')
def gis_curves_db():
    return render_template(r'gis/gis_curves_db.html')


@app.route('/gis/curves/input', methods=['GET', 'POST'])
@login_required
@roles_required('test_role')
def gis_curves_input():
    categories = GisCurveCategory.query.all()
    categories_len = len(categories)
    categories_list = list()
    for i in range(categories_len):
        print(i)
        categories_list.append((i+1, categories[i]))
    print(categories_list)

    return render_template(r'gis/gis_input_curves.html', categories_list=categories_list)


@app.route('/gis/curves/rename/<curve_id>', methods=['GET', 'POST'])
@login_required
@roles_required('test_role')
def gis_curves_rename(curve_id):
    method = GisCurve.query.filter_by(id=curve_id).first()
    print(method)
    return render_template(r'gis/gis_rename_curve.html', method=method)


# GTI
@app.route('/gti', methods=['GET', 'POST'])
@login_required
@roles_required('test_role')
def gti():

    return render_template(r'gti/gti_main_page.html')


@app.route('/gti/gti_tbl', methods=['GET', 'POST'])
@login_required
@roles_required('test_role')
def gti_tbl():
    gti_wellbores = Wellbore.query.filter_by(is_gti=True).order_by(desc(Wellbore.create_date)).all()
    return render_template(r'gti/gti_rate_tbl.html', wellbores=gti_wellbores)


@app.route('/gti/gti_quality_sheet/<gti_quality_sheet_id>', methods=['GET', 'POST'])
@login_required
@roles_required('test_role')
def gti_quality_sheet(gti_quality_sheet_id):
    return render_template(r'gti/gti_quality_sheet.html')


# return all customers
@app.route('/new_style_customers', methods=['GET', 'POST'])
def new_style_customers():
    customers = Customer.query.all()
    return render_template(r'new_style_customers.html', customers=customers)


# return 1 customer w info
@app.route('/new_style_customer/<id>', methods=['GET', 'POST'])
@login_required
def new_style_customer(id):
    customer = Customer.query.filter_by(id=id).first_or_404()
    well_types = WellType.query.all()
    return render_template(r'new_style_customer_page.html', customer=customer, well_types=well_types)


# return 1 customer w info
@app.route('/new_style_field/<id>', methods=['GET', 'POST'])
def new_style_field(id):
    field = Field.query.filter_by(id=id).first_or_404()
    well_types = WellType.query.all()
    return render_template(r'new_style_field.html', field=field, well_types=well_types)


@app.route('/new_style_pad/<id>', methods=['GET', 'POST'])
def new_style_pad(id):
    pad = Pad.query.filter_by(id=id).first()
    well_types = WellType.query.all()
    return render_template(r'new_style_pad.html', pad=pad, well_types=well_types)


@app.route('/new_style_well/<id>', methods=['GET', 'POST'])
def new_style_well(id):
    well = Well.query.filter_by(id=id).first()
    wellbore_types = WellboreType.query.all()
    return render_template(r'new_style_well.html', well=well, wellbore_types=wellbore_types)


@app.route('/new_style_wellbore/<id>', methods=['GET', 'POST'])
def new_style_wellbore(id):
    wellbore = Wellbore.query.filter_by(id=id).first()
    #wellbore_types = WellboreType.query.all()
    return render_template(r'new_style_wellbore.html', wellbore=wellbore)


@app.route('/quality_sheet/<id>', methods=['GET', 'POST'])
def quality_sheet(id):
    sheet = QualitySheet.query.filter_by(id=id).first()
    companies = ServiceCompany.query.all()
    return render_template(r'quality_sheet_bootstrap.html', sheet=sheet, companies=companies)


@app.route('/new_style_test', methods=['GET', 'POST'])
def new_style_test():
    return render_template(r'new_style_test.html')


@app.route('/save_to_db', methods=['post', 'get'])
def save_to_db():
    if request.method == 'POST':
        print(request.form)
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

        dot_by_meter = request.form.get('selected_dot').strip()

        second_table_result = request.form.get('second_table_result').strip()

        grade = request.form.get('grade').strip()
        """
        cl_to_add = QualitySheet(customer=customer, field=field, pad_num=pad_num, well_num=well_num,
                       service_company=service_company, well_section=well_section,
                       section_interval_beg=section_interval_beg, section_interval_end=section_interval_end,
                       section_diameter=section_diameter,
                       information=information, title_page=title_page, construct=construct, column_size=column_size,
                       well_chronology=well_chronology, drilling_fluid_info=drilling_fluid_info,
                       tool_composition=tool_composition, depth_control_data=depth_control_data,
                       directional_survey_data=directional_survey_data, main_record=main_record,
                       data_processing_and_tool_parameters=data_processing_and_tool_parameters,
                       second_record=second_record, curve_control_pad=curve_control_pad,
                       tool_calibration=tool_calibration,
                       las_file_design=las_file_design, las_file_design_well_section=las_file_design_well_section,
                       las_file_design_parameters_section=las_file_design_parameters_section,
                       las_file_design_curve_section=las_file_design_curve_section,
                       incorrect_RT_data=incorrect_RT_data, data_completeness=data_completeness,
                       data_transfer_settings=data_transfer_settings, curve_names=curve_names,
                       mnemonic_description=mnemonic_description, second_table_result=second_table_result,
                       dot_by_meter=dot_by_meter, grade=grade)
        db.session.add(cl_to_add)
        db.session.commit()
        method_row_len = len(request.form.getlist('method'))
        for row in range(method_row_len):
            method = request.form.getlist('method')[row]
            tool_type = request.form.getlist('tool_type')[row]  # переделать с getlist
            tool_num = request.form.getlist('tool_num')[row]
            calibration_date = request.form.getlist('calibration_date')[row]
            gis_date = request.form.getlist('gis_date')[row]
            receipt_date = request.form.getlist('receipt_date')[row]
            interval_beg = request.form.getlist('interval_beg')[row]
            interval_end = request.form.getlist('interval_end')[row]
            rt_coefficient = request.form.getlist('rt_coefficient')[row]
            no_data_coefficient = request.form.getlist('no_data_coefficient')[row]

            linkage_by_depth = request.form.getlist('linkage_by_depth')[row].strip()
            emissions = request.form.getlist('emissions')[row].strip()
            noise = request.form.getlist('noise')[row].strip()
            check_measurement = request.form.getlist('check_measurement')[row].strip()
            cross_plot_distribution = request.form.getlist('cross_plot_distribution')[row].strip()
            tool_indication = request.form.getlist('tool_indication')[row].strip()
            absolute_petrophysical_values = request.form.getlist('absolute_petrophysical_values')[row].strip()
            notes = request.form.getlist('notes')[row].strip()

            method_to_add_to_CL = Method(CL=cl_to_add,
                                         method=method, tool_type=tool_type, tool_num=tool_num,
                                         calibration_date=calibration_date, gis_date=gis_date,
                                         receipt_date=receipt_date, interval_beg=interval_beg,
                                         interval_end=interval_end, rt_coefficient=rt_coefficient,
                                         no_data_coefficient=no_data_coefficient,
                                         linkage_by_depth=linkage_by_depth,
                                         emissions=emissions, noise=noise, check_measurement=check_measurement,
                                         cross_plot_distribution=cross_plot_distribution,
                                         tool_indication=tool_indication,
                                         absolute_petrophysical_values=absolute_petrophysical_values, notes=notes,
                                         )
            db.session.add(method_to_add_to_CL)
            db.session.commit()
        """
        return redirect('/')


@app.route('/logger', methods=['GET'])
def logger():
    logger = Logger.query.all()
    return render_template('logger/logger_main_page.html', logger=logger)