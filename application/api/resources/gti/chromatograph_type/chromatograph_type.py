from application import ma, db
from application.models.gti.directory.chromatograph_type import GtiChromatographType
from marshmallow import fields as ma_fields


class GtiChromatographTypeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = GtiChromatographType
        sqla_session = db.session
    gti_rows = ma_fields.Nested('GtiTableRowGtiChromatographTypeSchema', default=[], many=True)


class GtiTableRowGtiChromatographTypeSchema(ma.SQLAlchemyAutoSchema):
    id = ma_fields.Int()
    chromatograph_type_id = ma_fields.Int()
    wellbore_id = ma_fields.Int()


chromatograph_type_schema = GtiChromatographTypeSchema()
chromatograph_types_schema = GtiChromatographTypeSchema(many=True)