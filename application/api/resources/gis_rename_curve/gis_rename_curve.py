from application import ma, db
from application.models.models import GisCurveRename
from marshmallow import fields as ma_fields


class GisCurveRenameSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = GisCurveRename
        sqla_session = db.session


gis_curve_rename_schema = GisCurveRenameSchema()
gis_curves_rename_schema = GisCurveRenameSchema(many=True)