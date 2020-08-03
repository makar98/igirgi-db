from flask_restful import Resource
from application.models.models import GisCurve
from .gis_curve import gis_curve_schema, gis_curves_schema
from flask_restful import reqparse
from application import db

from flask_security import login_required
from application.db_logger.methods import edit

class GisCurveApi(Resource):
    def get(self, gis_curve_id):
        gis_curve = GisCurve.query.filter_by(id=gis_curve_id).first_or_404()
        return gis_curve_schema.jsonify(gis_curve)

    @login_required
    def put(self, gis_curve_id):
        parser = reqparse.RequestParser()
        parser.add_argument('method')
        parser.add_argument('category_id')
        parser.add_argument('latin')
        parser.add_argument('curve_type')
        parser.add_argument('units')
        parser.add_argument('notes')
        args = parser.parse_args()

        gis_curve = GisCurve.query.filter_by(id=gis_curve_id).first()

        edit(editable_tbl=GisCurve, obj=gis_curve, args=args)

        return '', 201


class GisCurvesApi(Resource):
    def get(self):
        gis_curves = GisCurve.query.all()
        return gis_curves_schema.jsonify(gis_curves)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('method')
        parser.add_argument('category_id')
        parser.add_argument('latin')
        parser.add_argument('curve_type')
        parser.add_argument('units')
        parser.add_argument('notes')
        args = parser.parse_args()

        if  args['method']:
            gis_curve = GisCurve(method=args['method'], category_id=args['category_id'], latin=args['latin'],
                                 curve_type=args['curve_type'], units=args['units'], notes=args['notes'])
            db.session.add(gis_curve)
            db.session.commit()
            return gis_curve_schema.jsonify(gis_curve)
        else:
            return 'method is None', 400