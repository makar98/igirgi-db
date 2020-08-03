from application import ma, db
from application.models.models import  Wellbore, WellboreType
from marshmallow import fields as ma_fields


class WellboreSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Wellbore
        sqla_session = db.session
    wellbore_type = ma_fields.Nested('WellboreTypeSchema', default=[])


class WellboreTypeSchema(ma.SQLAlchemyAutoSchema):
    id = ma_fields.Int()
    name = ma_fields.Str()


wellbore_schema = WellboreSchema()
wellbores_schema = WellboreSchema(many=True)