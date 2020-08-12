from application import ma, db
from application.models.gis import GisCurve, GisCurveCategory
from marshmallow import fields as ma_fields


class GisCurveSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = GisCurve
        sqla_session = db.session


gis_curve_schema = GisCurveSchema()
gis_curves_schema = GisCurveSchema(many=True)