from flask_restful import Resource
from application.models.models import GisCurveRename
from .gis_rename_curve import gis_curve_rename_schema, gis_curves_rename_schema
from flask_restful import reqparse
from application import db

from flask_security import login_required
from application.db_logger.methods import edit

class GisRenameCurveApi(Resource):
    def get(self, curve_id):
        curve = GisCurveRename.query.filter_by(id=curve_id).first_or_404()
        return gis_curve_rename_schema.jsonify(curve)

    @login_required
    def put(self, curve_id):
        parser = reqparse.RequestParser()
        parser.add_argument('curve_id')
        parser.add_argument('latin')
        args = parser.parse_args()

        curve = GisCurveRename.query.filter_by(id=curve_id).first()

        edit(editable_tbl=GisCurveRename, obj=curve, args=args)

        return '', 201

class GisRenameCurvesApi(Resource):
    def get(self):
        curves = GisCurveRename.query.all()
        return gis_curves_rename_schema.jsonify(curves)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('curve_id')
        parser.add_argument('latin')
        args = parser.parse_args()

        if  args['latin']:
            curve = GisCurveRename(name=args['latin'], curve_id=args['curve_id'])
            db.session.add(curve)
            db.session.commit()
            return gis_curve_rename_schema.jsonify(curve)
        else:
            return 'latin is None', 400