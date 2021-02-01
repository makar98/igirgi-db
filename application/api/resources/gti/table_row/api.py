from flask_restful import Resource
from application.models.user import User
from application.models.gti.table_row import GtiTableRow
from application.models.models import Layer
from application.models.models import Wellbore, Well, Pad, Field, Customer, WellboreStatus, Layer
from .table_row import table_row_schema, table_rows_schema
from flask_restful import reqparse
from application import db
from flask import make_response
import json
from sqlalchemy import or_, and_, asc, desc
from datetime import datetime, timedelta

from flask_security import login_required, current_user

from application.db_logger import methods


class GtiTableRowApi(Resource):
    @login_required
    def get(self, table_row_id):
        table_row = GtiTableRow.query.filter_by(id=table_row_id).first_or_404()
        return table_row_schema.jsonify(table_row)

    @login_required
    def put(self, table_row_id):
        parser = reqparse.RequestParser()
        parser.add_argument('quality_id')  # +
        parser.add_argument('date_T3')  # +
        parser.add_argument('wellbore_status_id')  # +
        parser.add_argument('final_report_id')  # +
        parser.add_argument('service_company_id')  # +
        parser.add_argument('station_type_id')  # +
        parser.add_argument('degasser_type_id')  # +
        parser.add_argument('chromatograph_type_id')  # +
        parser.add_argument('factory_num')  # +
        parser.add_argument('notes')  # +
        parser.add_argument('layers_id')  # +
        parser.add_argument('frequency')  # +

        args = parser.parse_args()

        args['notes'] = args['notes'].strip()
        args['frequency'] = args['frequency'].strip()
        print(args['date_T3'])

        table_row = GtiTableRow.query.filter_by(id=table_row_id).first()

        ###########################
        # Редактирование ствола, к которму привязана строка ГТИ
        wellbore = table_row.wellbore
        wb_args = dict()
        if args['layers_id'] is not None:
            args['layers_id'] = json.loads(args['layers_id'])
            args['layers_id'] = sorted(list(map(int, args['layers_id'])))
            if args['layers_id'] != sorted([layer.id for layer in wellbore.layers_gti]):
                args['layers_gti'] = []
                for layer_id in args['layers_id']:
                    args['layers_gti'].append(Layer.query.filter_by(id=layer_id).first())
                wb_args['layers_gti'] = args['layers_gti']
                del args['layers_gti']  # Чтобы не пошло в лог по таблице GtiTableRow

        del args['layers_id']  # Чтобы не пошло в лог по таблице GtiTableRow

        if args['wellbore_status_id']:
            wb_args['wellbore_status_id'] = args['wellbore_status_id']
        methods.edit(editable_tbl=Wellbore, obj=wellbore, args=wb_args, user=current_user)
        del args['wellbore_status_id']
        # Конец редактирование ствола, к которму привязана строка ГТИ
        ###########################
        # Изменения в объект вносятся внутри methods.edit, чтобы не перебирать их дважды
        methods.edit(editable_tbl=GtiTableRow, obj=table_row, args=args, user=current_user)
        table_row.authors.append(current_user)

        return make_response(table_row_schema.jsonify(table_row), 201)

    """
    @login_required
    def delete(self, station_type_id):
        station_type = GtiTableRow.query.filter_by(id=station_type_id).first()
        name = station_type.name
        args = dict()
        args['name'] = name
        # Изменения в объект вносятся внутри methods.edit, чтобы не перебирать их дважды
        methods.delete(editable_tbl=GtiTableRow, obj=station_type, args=args, user=current_user)
        return '', 204
    """


class GtiTableRowsApi(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('users')

        parser.add_argument('date_interval')

        parser.add_argument('fields')
        parser.add_argument('layers')
        parser.add_argument('customers')
        parser.add_argument('service_companies')
        parser.add_argument('wellbore_statuses')
        parser.add_argument('qualities')

        args = parser.parse_args()
        # print(args)
        if args['users']:
            users_id = list(map(int, args['users'].split(',')))
        else:
            users_id = None

        if args['fields']:
            fields_id = args['fields'].split(',')
        else:
            fields_id = []
        if args['layers']:
            layers_id = args['layers'].split(',')
        else:
            layers_id = []
        if args['customers']:
            customers_id = args['customers'].split(',')
        else:
            customers_id = []
        if args['service_companies']:
            service_companies_id = args['service_companies'].split(',')
        else:
            service_companies_id = []
        if args['wellbore_statuses']:
            wellbore_statuses_id = args['wellbore_statuses'].split(',')
        else:
            wellbore_statuses_id = []
        if args['qualities']:
            qualities_id = args['qualities'].split(',')
        else:
            qualities_id = []

        date_interval = datetime(1990, 3, 5)
        if args['date_interval'] == 'last_hour':
            date_interval = datetime.now() - timedelta(hours=1)

        if args['date_interval'] == 'last_day':
            date_interval = datetime.now() - timedelta(days=1)

        if args['date_interval'] == 'last_week':
            date_interval = datetime.now() - timedelta(weeks=1)

        if args['date_interval'] == 'last_month':
            date_interval = datetime.now() - timedelta(days=30)

        if args['date_interval'] == 'all_time':
            date_interval = datetime(1990, 3, 5)

        query = db.session.query(GtiTableRow).filter(GtiTableRow.edit_date >= date_interval)

        query = query \
            .join(Wellbore, Wellbore.id == GtiTableRow.wellbore_id) \
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

        gti_rows = query.all()
        print(gti_rows)
        return table_rows_schema.jsonify(gti_rows)

    """
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        args = parser.parse_args()

        if  args['name']:
            station_type = GtiTableRow(name=args['name'])
            db.session.add(station_type)
            db.session.commit()

            methods.create(editable_tbl=GtiTableRow, obj=station_type, args=args, user=current_user)
            return table_row_schema.jsonify(station_type)
        else:
            return 'Row is None', 400
    """
