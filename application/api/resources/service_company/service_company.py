from application import ma, db
from application.models.models import ServiceCompany, Tool
from marshmallow import fields as ma_fields


class ServiceCompanySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ServiceCompany
        sqla_session = db.session
    tools = ma_fields.Nested('ServiceCompanyToolSchema', default=[], many=True)


class ServiceCompanyToolSchema(ma.SQLAlchemyAutoSchema):
    id = ma_fields.Int()
    service_company_id = ma_fields.Int()
    name = ma_fields.Str()
    tool_type = ma_fields.Str()


class ToolSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Tool
        sqla_session = db.session
    service_companySchema = ma_fields.Nested('ToolServiceCompanySchema', default=[])


class ToolServiceCompanySchema(ma.SQLAlchemyAutoSchema):
    customer_id = ma_fields.Int()
    id = ma_fields.Int()
    name = ma_fields.Str()


service_company_schema = ServiceCompanySchema()
service_companies_schema = ServiceCompanySchema(many=True)