from application import ma, db
from application.models.gti.parameter import GtiParameter
from application.models.gti.format import GtiFormat
from marshmallow import fields as ma_fields


class CompanySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = GtiParameter
        sqla_session = db.session
    gti_rows = ma_fields.Nested('TableRowSchema', default=[], many=True)


class TableRowSchema(ma.SQLAlchemyAutoSchema):
    id = ma_fields.Int()
    service_company_id = ma_fields.Int()
    wellbore_id = ma_fields.Int()


service_company_schema = CompanySchema()
service_companies_schema = CompanySchema(many=True)