from flask_restful import Resource
from application.models.gis import GisCurveCategory
from .gis_curve_category import gis_curve_category_schema, gis_curve_categories_schema
from flask_restful import reqparse
from application import db

from flask_security import login_required
from application.db_logger.methods import edit

class GisCurveCategoryApi(Resource):
    def get(self, customer_id):
        category = GisCurveCategory.query.filter_by(id=customer_id).first_or_404()
        return gis_curve_category_schema.jsonify(category)

    @login_required
    def put(self, customer_id):
        parser = reqparse.RequestParser()
        parser.add_argument('category')
        args = parser.parse_args()

        category = GisCurveCategory.query.filter_by(id=customer_id).first()

        edit(editable_tbl=GisCurveCategory, obj=category, args=args)

        return '', 201


class GisCurveCategoriesApi(Resource):
    def get(self):
        categories = GisCurveCategory.query.all()
        return gis_curve_categories_schema.jsonify(categories)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('category')
        args = parser.parse_args()

        if  args['category']:
            category = GisCurveCategory(name=args['category'])
            db.session.add(category)
            db.session.commit()
            return gis_curve_category_schema.jsonify(category)
        else:
            return 'category is None', 400