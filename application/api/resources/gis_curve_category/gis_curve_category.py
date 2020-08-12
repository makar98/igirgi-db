from application import ma, db
from application.models.gis import GisCurve, GisCurveCategory
from marshmallow import fields as ma_fields


class GisCurveCategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = GisCurveCategory
        sqla_session = db.session
    curves = ma_fields.Nested('CustomerFieldSchema', default=[], many=True)


class GisCurveCategoryGisCurveSchema(ma.SQLAlchemyAutoSchema):
    id = ma_fields.Int()
    customer_id = ma_fields.Int()
    name = ma_fields.Str()


class GisCurveSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = GisCurve
        sqla_session = db.session
    category = ma_fields.Nested('GisCurveGisCurveCategorySchema', default=[])


class GisCurveGisCurveCategorySchema(ma.SQLAlchemyAutoSchema):
    customer_id = ma_fields.Int()
    id = ma_fields.Int()
    name = ma_fields.Str()


gis_curve_category_schema = GisCurveCategorySchema()
gis_curve_categories_schema = GisCurveCategorySchema(many=True)