from application import app, db
from application.models.models import ServiceCompany, Tool, QualitySheet, Method, \
    FilePath, CustomerEmail, CompanyEmail

from application.models.models import Customer
from application.models.models import Field
from application.models.models import Layer
from application.models.models import Well
from application.models.models import WellType
from application.models.models import QualitySheet
from application.models.models import GisCurve
from application.models.models import GisCurveCategory
from application.models.user import User, Role
from application.models.models import GtiTableRow
from application.models.logger import Logger, EditableField


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Customer': Customer, 'Field': Field, 'Layer': Layer, 'Well': Well, 'WellType': WellType,
            'Tool': Tool, 'QualitySheet': QualitySheet,
            'ServiceCompany': ServiceCompany,
            'QualitySheet': QualitySheet, 'Method': Method, 'FilePath': FilePath, 'CustomerEmail': CustomerEmail,
            'CompanyEmail': CompanyEmail, 'User': User, 'Role': Role,
            'GisCurve': GisCurve, 'GisCurveCategory': GisCurveCategory,
            'GtiTableRow': GtiTableRow,
            'Logger': Logger, 'EditableField': EditableField}


if __name__ == '__main__':
    #  app.config['SECRET_KEY'] = '18011998'
    #  app.config['UPLOAD_FOLDER'] =
    app.run(debug=True)#  port='12006', host='10.23.124.44', debug=True)
