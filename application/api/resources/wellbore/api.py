from flask_restful import Resource
from application.models.models import Well
from application.models.models import Wellbore
from application.models.gis import QualitySheet
from application.models.gti.table_row import GtiTableRow
from application.models.gti.quality_sheet.quality_sheet import GtiQualitySheet
from application.models.user import User
from .wellbore import wellbore_schema, wellbores_schema
from flask_restful import reqparse
from application import db
from flask import make_response

from flask_security import login_required, current_user
from application.db_logger import methods

class WellboreApi(Resource):
    def get(self, wellbore_id):
        wellbore = Wellbore.query.filter_by(id=wellbore_id).first_or_404()
        return wellbore_schema.jsonify(wellbore)

    @login_required
    def put(self, wellbore_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        parser.add_argument('wellbore_type_id')
        args = parser.parse_args()

        wellbore = Wellbore.query.filter_by(id=wellbore_id).first()

        # Изменения в объект вносятся внутри methods.edit, чтобы не перебирать их дважды
        methods.edit(editable_tbl=Wellbore, obj=wellbore, args=args, user=current_user)

        return make_response(wellbore_schema.jsonify(wellbore), 201)

    @login_required
    def delete(self, wellbore_id):
        wellbore = Wellbore.query.filter_by(id=wellbore_id).first()
        name = wellbore.name
        args = dict()
        args['name'] = name
        # Изменения в объект вносятся внутри methods.edit, чтобы не перебирать их дважды
        methods.delete(editable_tbl=Wellbore, obj=wellbore, args=args, user=current_user)
        return '', 204

class WellboresApi(Resource):
    def get(self):
        wellbores = Wellbore.query.all()
        return wellbores_schema.jsonify(wellbores)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_id')
        parser.add_argument('name')
        parser.add_argument('well_id')
        parser.add_argument('wellbore')
        parser.add_argument('wellbore_type_id')
        parser.add_argument('is_gis')
        parser.add_argument('is_gti')
        args = parser.parse_args()
        if  args['wellbore']:
            well_id = int(args['well_id'])
            wellbore = Wellbore(name=args['wellbore'], well_id=well_id,
                        wellbore_type_id=int(args['wellbore_type_id']),
                        is_gis=bool(args['is_gis']), is_gti=bool(args['is_gti']))

            well = Well.query.filter_by(id=well_id).first()

            db.session.add(wellbore)
            db.session.flush()

            if int(args['is_gis']) == 1:
                gis_quality_sheet = QualitySheet(customer_id=well.customer.id, field_id=well.field.id, pad_id=well.pad.id,
                                              well_id=well.id, well_type_id=well.well_type_id, wellbore_id=wellbore.id,
                                              wellbore_type_id=wellbore.wellbore_type_id)
                db.session.add(gis_quality_sheet)

            if int(args['is_gti']) == 1:
                gti_table_row = GtiTableRow(wellbore_id=wellbore.id)
                db.session.add(gti_table_row)
                author = User.query.filter_by(id=int(args['user_id'])).first()
                gti_table_row.authors.append(author)
                db.session.flush()

                gis_quality_sheet = GtiQualitySheet(gti_table_row_id=gti_table_row.id)
                db.session.add(gis_quality_sheet)


            db.session.commit()

            methods.create(editable_tbl=Wellbore, obj=wellbore, args=args, user=current_user)
            return wellbore_schema.jsonify(wellbore)
        else:
            return '', 400