from application import ma, db
from application.models.models import Customer, Field
from marshmallow import fields as ma_fields


class CustomerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Customer
        sqla_session = db.session
    fields = ma_fields.Nested('CustomerFieldSchema', default=[], many=True)


class CustomerFieldSchema(ma.SQLAlchemyAutoSchema):
    id = ma_fields.Int()
    customer_id = ma_fields.Int()
    name = ma_fields.Str()


class FieldSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Field
        sqla_session = db.session
    customer = ma_fields.Nested('FieldCustomerSchema', default=[])


class FieldCustomerSchema(ma.SQLAlchemyAutoSchema):
    customer_id = ma_fields.Int()
    id = ma_fields.Int()
    name = ma_fields.Str()


customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)