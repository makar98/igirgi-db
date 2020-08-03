from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


# Импорт моделей делать после db
# https://stackoverflow.com/questions/50308051/importerror-cannot-import-name-db
from application.models.models import Tool, QualitySheet, ServiceCompany
from application.models.models import Customer
from application.models.models import Field
from application.models.models import Pad
from application.models.models import Layer
from application.models.models import Well
from application.models.models import WellboreType
from application.models.models import Wellbore

from application.models.user import User, Role
from application.models.models import GtiTableRow


#from application.models.UserSearchSettings import UserSearchSettings


class FieldView(ModelView):
    can_delete = False
    column_exclude_list = ['date_add', ]


class CustomerView(ModelView):
    can_delete = True
    can_export = True
    export_types = ['xlsx']


class QualitySheetView(ModelView):
    can_delete = False
    can_export = True
    export_types = ['xlsx']


def create_admin(app, db):
    admin = Admin(app, name='Лист оценки качества', template_mode='bootstrap3')
    admin.add_view(CustomerView(Customer, db.session))
    admin.add_view(FieldView(Field, db.session))
    admin.add_view(ModelView(Tool, db.session))
    admin.add_view(ModelView(ServiceCompany, db.session))
    admin.add_view(QualitySheetView(QualitySheet, db.session))
    admin.add_view(ModelView(Layer, db.session))
    admin.add_view(ModelView(Well, db.session))
    admin.add_view(ModelView(Pad, db.session))
    admin.add_view(ModelView(Wellbore, db.session))
    admin.add_view(ModelView(WellboreType, db.session))

    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Role, db.session))
    admin.add_view(ModelView(GtiTableRow, db.session))
