from flask_restful import Resource
from application.models.models import ServiceCompany
from .service_company import service_company_schema, service_companies_schema

from flask_security import login_required
from application.db_logger.methods import edit

class ServiceCompanyApi(Resource):
    def get(self, service_company_id):
        service_company = ServiceCompany.query.filter_by(id=service_company_id).first_or_404()
        return service_company_schema.jsonify(service_company)

    """
    @login_required
    def put(self, field_id):
        parser = reqparse.RequestParser()
        parser.add_argument('field')
        parser.add_argument('customer_id')
        args = parser.parse_args()

        field = Field.query.filter_by(id=field_id).first()

        edit(editable_tbl=Field, obj=field, args=args)

        return '', 201
    """

class ServiceCompaniesApi(Resource):
    def get(self):
        service_companies = ServiceCompany.query.all()
        return service_companies_schema.jsonify(service_companies)

