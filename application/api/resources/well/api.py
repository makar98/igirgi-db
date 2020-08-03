from flask_restful import Resource
from application.models.models import Well
from .well import well_schema, wells_schema
from flask_restful import reqparse
from application import db

from flask_security import login_required
from application.db_logger.methods import edit

class WellApi(Resource):
    def get(self, well_id):
        well = Well.query.filter_by(id=well_id).first_or_404()
        return well_schema.jsonify(well)

    @login_required
    def put(self, well_id):
        parser = reqparse.RequestParser()
        parser.add_argument('customer_id')
        parser.add_argument('field_id')
        parser.add_argument('pad_id')
        parser.add_argument('name')
        parser.add_argument('well_type_id')
        args = parser.parse_args()

        well = Well.query.filter_by(id=well_id).first()

        edit(editable_tbl=Well, obj=well, args=args)

        return '', 201


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
            return well_schema.jsonify(well)
        else:
            return '', 400