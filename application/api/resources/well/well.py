from application import ma, db
from application.models.models import Well, Wellbore
from marshmallow import fields as ma_fields


class WellSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Well
        sqla_session = db.session

    well_type = ma_fields.Str()
    wellbores = ma_fields.Nested('WellWellboreSchema', default=[], many=True)


class WellWellboreSchema(ma.SQLAlchemyAutoSchema):
    id = ma_fields.Int()
    well_id = ma_fields.Int()
    name = ma_fields.Str()


class WellboreSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Wellbore
        sqla_session = db.session
    well = ma_fields.Nested('WellboreWellSchema', default=[])


class WellboreWellSchema(ma.SQLAlchemyAutoSchema):
    well_id = ma_fields.Int()
    id = ma_fields.Int()
    name = ma_fields.Str()


well_schema = WellSchema()
wells_schema = WellSchema(many=True)