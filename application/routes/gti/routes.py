from application import app, db
from flask import render_template, request

from sqlalchemy import asc, desc

from application.models.models import Wellbore, Well, Pad, Field, Customer, \
    WellboreStatus, Layer, Suite, WellboreType, WellType

from application.models.gti.format import GtiFormat
from application.models.gti.parameter import GtiParameter

from application.models.gti.table_row import GtiTableRowQuality
from application.models.gti.quality_sheet.quality_sheet import GtiQualitySheet
from application.models.gti.quality_sheet.final_report import GtiFinalReport
from application.models.gti.directory.chromatograph_type import GtiChromatographType
from application.models.gti.directory.degasser_type import GtiDegasserType
from application.models.gti.directory.station_type import GtiStationType
from application.models.gti.directory.service_company import GtiServiceCompany

from application.models.models import WellboreStatus, Field
from application.models.user import User
from application.models.models import Suite

from datetime import datetime, timedelta


from flask_security import login_required, roles_required

from application.routes.gti.queries import *


@app.route('/gti', methods=['GET', 'POST'])
@login_required
@roles_required('test_role')
def gti():
    return render_template(r'gti/gti_main_page.html')


@app.route('/gti/tbl', methods=['GET', 'POST'])
@login_required
@roles_required('test_role')
def gti_tbl():

    if request.args.get('filter') is not None:
        if request.args.get('users'):
            users_id = list(map(int, request.args.get('users').split(',')))
        else:
            users_id = None

        if request.args.get('fields'):
            fields_id = request.args.get('fields').split(',')
        else:
            fields_id = []
        if request.args.get('layers'):
            layers_id = request.args.get('layers').split(',')
        else:
            layers_id = []
        if request.args.get('customers'):
            customers_id = request.args.get('customers').split(',')
        else:
            customers_id = []
        if request.args.get('service_companies'):
            service_companies_id = request.args.get('service_companies').split(',')
        else:
            service_companies_id = []
        if request.args.get('wellbore_statuses'):
            wellbore_statuses_id = request.args.get('wellbore_statuses').split(',')
        else:
            wellbore_statuses_id = []
        if request.args.get('qualities'):
            qualities_id = request.args.get('qualities').split(',')
        else:
            qualities_id = []

        date_interval = datetime(1990, 3, 5)
        if request.args.get('date_interval') == 'last_hour':
            date_interval = datetime.now() - timedelta(hours=1)

        if request.args.get('date_interval') == 'last_day':
            date_interval = datetime.now() - timedelta(days=1)

        if request.args.get('date_interval') == 'last_week':
            date_interval = datetime.now() - timedelta(weeks=1)

        if request.args.get('date_interval') == 'last_month':
            date_interval = datetime.now() - timedelta(days=30)

        if request.args.get('date_interval') == 'all_time':
            date_interval = datetime(1990, 3, 5)

        query = db.session.query(Wellbore).filter(Wellbore.is_gti == True)
        query = query.filter(GtiTableRow.edit_date >= date_interval)

        query = query \
            .join(GtiTableRow, GtiTableRow.wellbore_id == Wellbore.id) \
            .join(Well, Well.id == Wellbore.well_id) \
            .join(Customer, Customer.id == Well.customer_id) \
            .filter(Customer.id.in_(customers_id))

        query = query \
            .join(Pad, Pad.id == Well.pad_id) \
            .join(Field, Field.id == Pad.field_id). \
            filter(Field.id.in_(fields_id))

        query = query \
            .join(WellboreStatus, WellboreStatus.id == Wellbore.wellbore_status_id) \
            .filter(WellboreStatus.id.in_(wellbore_statuses_id))

        query = query.filter(GtiTableRow.authors.any(User.id.in_(users_id)))
        query = query.filter(Wellbore.layers_gti.any(Layer.id.in_(layers_id)))
        query = query.filter(GtiTableRow.service_company_id.in_(service_companies_id))
        query = query.filter(GtiTableRow.quality_id.in_(qualities_id))

        gti_wellbores = query.all()
        print(gti_wellbores)
    else:
        gti_wellbores = Wellbore.query.filter_by(is_gti=True).order_by(desc(Wellbore.create_date)).all()
    wellbore_types = WellboreType.query.all()
    well_types = WellType.query.all()
    wellbore_statuses = WellboreStatus.query.all()
    customers = Customer.query.all()
    service_companies = GtiServiceCompany.query.all()
    suites = Suite.query.all()
    station_types = GtiStationType.query.all()
    degasser_types = GtiDegasserType.query.all()
    chromatograph_types = GtiChromatographType.query.all()
    qualities = GtiTableRowQuality.query.all()
    final_reports = GtiFinalReport.query.all()

    # SEARCH
    fields = Field.query.all()
    users = User.query.all()
    return render_template(r'gti/gti_rate_tbl.html',
                           wellbores=gti_wellbores,
                           wellbore_types=wellbore_types,
                           well_types=well_types,
                           customers=customers,
                           service_companies=service_companies,
                           suites=suites,
                           station_types=station_types,
                           degasser_types=degasser_types,
                           chromatograph_types=chromatograph_types,
                           qualities=qualities,
                           final_reports=final_reports,
                           wellbore_statuses=wellbore_statuses,
                           fields=fields,
                           users=users)


@app.route('/gti/quality_sheet/<gti_quality_sheet_id>', methods=['GET', 'POST'])
@login_required
@roles_required('test_role')
def gti_quality_sheet(gti_quality_sheet_id):
    param = GtiParameter.query.all()
    quality_sheet = GtiQualitySheet.query.filter_by(id=gti_quality_sheet_id).first_or_404()
    return render_template(r'gti/quality_sheet.html',
                           param=param,
                           quality_sheet=quality_sheet)


@app.route('/gti/directory', methods=['GET', 'POST'])
@login_required
@roles_required('test_role')
def gti_directory():
    return render_template(r'gti/directory/directory.html')


@app.route('/gti/directory/parameters', methods=['GET', 'POST'])
@login_required
@roles_required('test_role')
def gti_parameters():
    parameters = GtiParameter.query.all()
    return render_template(r'gti/directory/parameters.html', parameters=parameters)


@app.route('/gti/directory/parameter/<int:parameter_id>', methods=['GET', 'POST'])
@login_required
@roles_required('test_role')
def gti_parameter(parameter_id):
    parameter = GtiParameter.query.filter_by(id=parameter_id).first_or_404()
    return render_template(r'gti/directory/parameter.html', parameter=parameter)


@app.route('/gti/directory/format/<int:format_id>', methods=['GET', 'POST'])
@login_required
@roles_required('test_role')
def gti_format(format_id):
    format = GtiFormat.query.filter_by(id=format_id).first_or_404()
    return render_template(r'gti/directory/format.html', format=format)


@app.route('/gti/directory/service_companies', methods=['GET', 'POST'])
@login_required
@roles_required('test_role')
def gti_service_companies():
    service_companies = GtiServiceCompany.query.all()
    return render_template(r'gti/directory/service_companies.html', service_companies=service_companies)


@app.route('/gti/directory/service_company/<int:company_id>', methods=['GET', 'POST'])
@login_required
@roles_required('test_role')
def gti_service_company(company_id):
    company = GtiServiceCompany.query.filter_by(id=company_id).first_or_404()
    return render_template(r'gti/directory/service_company.html', company=company)


@app.route('/gti/directory/station_types', methods=['GET'])
@login_required
@roles_required('test_role')
def gti_station_types():
    station_types = GtiStationType.query.all()
    return render_template(r'gti/directory/station_types.html', station_types=station_types)


@app.route('/gti/directory/station_type/<int:type_id>', methods=['GET'])
@login_required
@roles_required('test_role')
def gti_station_type(type_id):
    station_type = GtiStationType.query.filter_by(id=type_id).first_or_404()
    return render_template(r'gti/directory/station_type.html', type=station_type)


@app.route('/gti/directory/chromatograph_type', methods=['GET'])
@login_required
@roles_required('test_role')
def gti_chromatograph_types():
    chromatograph_types = GtiChromatographType.query.all()
    return render_template(r'gti/directory/chromatograph_types.html', chromatograph_types=chromatograph_types)


@app.route('/gti/directory/chromatograph_type/<int:type_id>', methods=['GET'])
@login_required
@roles_required('test_role')
def gti_chromatograph_type(type_id):
    chromatograph_type = GtiChromatographType.query.filter_by(id=type_id).first_or_404()
    return render_template(r'gti/directory/chromatograph_type.html', type=chromatograph_type)


@app.route('/gti/directory/degasser_type', methods=['GET'])
@login_required
@roles_required('test_role')
def gti_degasser_types():
    degasser_types = GtiDegasserType.query.all()
    return render_template(r'gti/directory/degasser_types.html', degasser_types=degasser_types)


@app.route('/gti/directory/degasser_type/<int:type_id>', methods=['GET'])
@login_required
@roles_required('test_role')
def gti_degasser_type(type_id):
    degasser_type = GtiDegasserType.query.filter_by(id=type_id).first_or_404()
    return render_template(r'gti/directory/degasser_type.html', type=degasser_type)

