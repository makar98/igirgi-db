from flask_restful import Resource
from application.models.models import Well
from .well import well_schema, wells_schema
from flask_restful import reqparse
from application import db
from flask import make_response

from flask_security import login_required, current_user
from application.db_logger import methods

class WellApi(Resource):
    def get(self, well_id):
        well = Well.query.filter_by(id=well_id).first_or_404()
        return well_schema.jsonify(well)

    @login_required
    def put(self, well_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        parser.add_argument('well_type_id')
        args = parser.parse_args()

        well = Well.query.filter_by(id=well_id).first()


        # Изменения в объект вносятся внутри methods.edit, чтобы не перебирать их дважды
        methods.edit(editable_tbl=Well, obj=well, args=args, user=current_user)

        return make_response(well_schema.jsonify(well), 201)

    @login_required
    def delete(self, well_id):
        well = Well.query.filter_by(id=well_id).first()
        name = well.name
        args = dict()
        args['name'] = name
        # Изменения в объект вносятся внутри methods.edit, чтобы не перебирать их дважды
        methods.delete(editable_tbl=Well, obj=well, args=args, user=current_user)
        return '', 204


class WellsApi(Resource):
    def get(self):
        wells = Well.query.all()
        return wells_schema.jsonify(wells)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('customer_id')
        parser.add_argument('field_id')
        parser.add_argument('pad_id')
        parser.add_argument('well')
        parser.add_argument('well_type_id')
        args = parser.parse_args()

        if  args['well']:
            well = Well(name=args['well'], customer_id=int(args['customer_id']),
                        field_id=int(args['field_id']), pad_id=int(args['pad_id']),
                        well_type_id=int(args['well_type_id']))
            db.session.add(well)
            db.session.commit()

            methods.create(editable_tbl=Well, obj=well, args=args, user=current_user)
            return well_schema.jsonify(well)
        else:
            return '', 400