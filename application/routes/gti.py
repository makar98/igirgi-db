from application import app
from flask import render_template

from sqlalchemy import asc, desc

from application.models.models import Customer

from application.models.models import Wellbore
from application.models.models import WellboreType

from application.models.models import WellType

from application.models.gti.format import GtiFormat
from application.models.gti.parameter import GtiParameter

from application.models.gti.quality_sheet.quality_sheet import GtiQualitySheet
from application.models.gti.directory.service_company import GtiServiceCompany
from application.models.gti.directory.chromatograph_type import GtiChromatographType
from application.models.gti.directory.degasser_type import GtiDegasserType
from application.models.gti.directory.station_type import GtiStationType
from application.models.gti.directory.service_company import GtiServiceCompany

from application.models.models import WellboreStatus
from application.models.models import Suite


from flask_security import login_required, roles_required


@app.route('/gti', methods=['GET', 'POST'])
@login_required
@roles_required('test_role')
def gti():
    return render_template(r'gti/gti_main_page.html')


@app.route('/gti/tbl', methods=['GET', 'POST'])
@login_required
@roles_required('test_role')
def gti_tbl():
    gti_wellbores = Wellbore.query.filter_by(is_gti=True).order_by(desc(Wellbore.create_date)).all()
    wellbore_types = WellboreType.query.all()
    well_types = WellType.query.all()
    wellbore_statuses = WellboreStatus.query.all()
    customer = Customer.query.all()
    service_companies = GtiServiceCompany.query.all()
    suites = Suite.query.all()
    station_types = GtiStationType.query.all()
    degasser_types = GtiDegasserType.query.all()
    chromatograph_types = GtiChromatographType.query.all()
    for wb in gti_wellbores:
        print(wb.gti_row.gti_quality_sheet)
    return render_template(r'gti/gti_rate_tbl.html',
                           wellbores=gti_wellbores,
                           wellbore_types=wellbore_types,
                           well_types=well_types,
                           customer=customer,
                           service_companies=service_companies,
                           suites=suites,
                           station_types=station_types,
                           degasser_types=degasser_types,
                           chromatograph_types=chromatograph_types)


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

