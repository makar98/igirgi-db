from application import ma, db
from application.models.models import Field, Pad
from marshmallow import fields as ma_fields


class FieldSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Field
        sqla_session = db.session
    pads = ma_fields.Nested('FieldPadSchema', default=[], many=True)


class FieldPadSchema(ma.SQLAlchemyAutoSchema):
    id = ma_fields.Int()
    customer_id = ma_fields.Int()
    field_id = ma_fields.Int()
    name = ma_fields.Str()


class PadSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Pad
        sqla_session = db.session
    customer = ma_fields.Nested('PadFieldSchema', default=[])


class PadFieldSchema(ma.SQLAlchemyAutoSchema):
    field_id = ma_fields.Int()
    id = ma_fields.Int()
    name = ma_fields.Str()


field_schema = FieldSchema()
fields_schema = FieldSchema(many=True)