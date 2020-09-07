from application import ma, db
from marshmallow import fields as ma_fields

from application.models.models import Suite


class SuiteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Suite
        sqla_session = db.session
    layers = ma_fields.Nested('SuiteLayerSchema', default=[], many=True)


class SuiteLayerSchema(ma.SQLAlchemyAutoSchema):
    id = ma_fields.Int()
    suite_id = ma_fields.Int()
    name = ma_fields.Str()



suite_schema = SuiteSchema()
suites_schema = SuiteSchema(many=True)