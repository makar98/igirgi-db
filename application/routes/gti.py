from application import app
from flask import render_template

from sqlalchemy import asc, desc

from application.models.models import Customer

from application.models.models import Wellbore
from application.models.models import WellboreType

from application.models.gti.format import GtiFormat
from application.models.gti.parameter import GtiParameter


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
    customers = Customer.query.all()
    print(gti_wellbores)
    print(gti_wellbores[3].well.customer.name)
    print(gti_wellbores[3].name)
    print(gti_wellbores[3].id)
    for w in gti_wellbores:
        print(w.gti_row.authors)
    return render_template(r'gti/gti_rate_tbl.html',
                           wellbores=gti_wellbores,
                           wellbore_types=wellbore_types,
                           customers=customers)


@app.route('/gti/quality_sheet/<gti_quality_sheet_id>', methods=['GET', 'POST'])
@login_required
@roles_required('test_role')
def gti_quality_sheet(gti_quality_sheet_id):
    param = GtiParameter.query.all()
    return render_template(r'gti/quality_sheet.html', param=param)


@app.route('/gti/directory', methods=['GET', 'POST'])
@login_required
@roles_required('test_role')
def gti_directory():
    return render_template(r'gti/directory.html')


@app.route('/gti/parameters', methods=['GET', 'POST'])
@login_required
@roles_required('test_role')
def gti_parameters():
    parameters = GtiParameter.query.all()
    return render_template(r'gti/parameters.html', parameters=parameters)


@app.route('/gti/parameter/<int:parameter_id>', methods=['GET', 'POST'])
@login_required
@roles_required('test_role')
def gti_parameter(parameter_id):
    parameter = GtiParameter.query.filter_by(id=parameter_id).first_or_404()
    return render_template(r'gti/parameter.html', parameter=parameter)


@app.route('/gti/format/<int:format_id>', methods=['GET', 'POST'])
@login_required
@roles_required('test_role')
def gti_format(format_id):
    format = GtiFormat.query.filter_by(id=format_id).first_or_404()
    return render_template(r'gti/format.html', format=format)


@app.route('/gti/test', methods=['GET', 'POST'])
@login_required
@roles_required('test_role')
def gti_test():
    return render_template(r'gti/test.html')