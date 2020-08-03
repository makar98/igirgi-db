from application import ma, db
from application.models.models import Customer, Field, Pad, Well
from marshmallow import fields as ma_fields


class CustomerFullDataSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Customer
        sqla_session = db.session
    fields = ma_fields.Nested('CustomerFieldFullDataSchema', default=[], many=True)


class CustomerFieldFullDataSchema(ma.SQLAlchemyAutoSchema):
    id = ma_fields.Int()
    customer_id = ma_fields.Int()
    name = ma_fields.Str()
    pads = ma_fields.Nested('FieldPadFullDataSchema', default=[], many=True)


class FieldFullDataSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Field
        sqla_session = db.session
    customer = ma_fields.Nested('FieldCustomerFullDataSchema', default=[])


class FieldCustomerFullDataSchema(ma.SQLAlchemyAutoSchema):
    customer_id = ma_fields.Int()
    id = ma_fields.Int()
    name = ma_fields.Str()


class FieldPadFullDataSchema(ma.SQLAlchemyAutoSchema):
    field_id = ma_fields.Int()
    id = ma_fields.Int()
    name = ma_fields.Str()
    wells = ma_fields.Nested('PadWellFullDataSchema', default=[], many=True)

class PadFullDataSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Pad
        sqla_session = db.session
        fields = ("id", "name", "wells")
    field = ma_fields.Nested('PadFieldFullDataSchema', default=[])


class PadFieldFullDataSchema(ma.SQLAlchemyAutoSchema):
    field_id = ma_fields.Int()
    id = ma_fields.Int()
    pad = ma_fields.Str()


class WellFullDataSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Well
        sqla_session = db.session
        fields = ("id", "name")


class PadWellFullDataSchema(ma.SQLAlchemyAutoSchema):
    field_id = ma_fields.Int()
    id = ma_fields.Int()
    name = ma_fields.Str()


customer_full_data_schema = CustomerFullDataSchema()
customers_full_data_schema = CustomerFullDataSchema(many=True)
