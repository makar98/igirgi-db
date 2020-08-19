from application import ma, db
from application.models.gti.directory.degasser_type import GtiDegasserType
from marshmallow import fields as ma_fields


class GtiDegasserTypeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = GtiDegasserType
        sqla_session = db.session
    gti_rows = ma_fields.Nested('GtiTableRowGtiGtiDegasserTypeSchema', default=[], many=True)


class GtiTableRowGtiGtiDegasserTypeSchema(ma.SQLAlchemyAutoSchema):
    id = ma_fields.Int()
    chromatograph_type_id = ma_fields.Int()
    wellbore_id = ma_fields.Int()


degasser_type_schema = GtiDegasserTypeSchema()
degasser_types_schema = GtiDegasserTypeSchema(many=True)