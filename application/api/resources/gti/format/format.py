from application import ma, db
from application.models.gti.format import GtiFormat
from application.models.gti.parameter import GtiParameter
from marshmallow import fields as ma_fields


class FormatSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = GtiFormat
        sqla_session = db.session

format_schema = FormatSchema()
formats_schema = FormatSchema(many=True)