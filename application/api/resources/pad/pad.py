from application import ma, db
from application.models.models import Pad, Well
from marshmallow import fields as ma_fields


class PadSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Pad
        sqla_session = db.session
    wells = ma_fields.Nested('PadWellSchema', default=[], many=True)


class PadWellSchema(ma.SQLAlchemyAutoSchema):
    id = ma_fields.Int()
    customer_id = ma_fields.Int()
    field_id = ma_fields.Int()
    name = ma_fields.Str()
    well_type = ma_fields.Str()


class WellSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Well
        sqla_session = db.session
    customer = ma_fields.Nested('WellPadSchema', default=[])


class WellPadSchema(ma.SQLAlchemyAutoSchema):
    field_id = ma_fields.Int()
    id = ma_fields.Int()
    name = ma_fields.Str()


pad_schema = PadSchema()
pads_schema = PadSchema(many=True)