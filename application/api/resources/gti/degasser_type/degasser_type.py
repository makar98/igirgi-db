from application import ma, db
from application.models.gti.parameter import GtiParameter
from application.models.gti.format import GtiFormat
from marshmallow import fields as ma_fields


class ParameterSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = GtiParameter
        sqla_session = db.session
    fields = ma_fields.Nested('ParameterFormatSchema', default=[], many=True)


class ParameterFormatSchema(ma.SQLAlchemyAutoSchema):
    id = ma_fields.Int()
    parameter_id = ma_fields.Int()
    name = ma_fields.Str()


class FormatSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = GtiFormat
        sqla_session = db.session
    parameter = ma_fields.Nested('FormatParameterSchema', default=[])


class FormatParameterSchema(ma.SQLAlchemyAutoSchema):
    format_id = ma_fields.Int()
    id = ma_fields.Int()
    name = ma_fields.Str()


parameter_schema = ParameterSchema()
parameters_schema = ParameterSchema(many=True)