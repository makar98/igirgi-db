from flask_restful import Resource
from application.models.gti.directory.service_company import GtiServiceCompany
from .service_company import service_company_schema, service_companies_schema
from flask_restful import reqparse
from application import db
from flask import make_response

from flask_security import login_required, current_user

from application.db_logger import methods

class GtiServiceCompanyApi(Resource):
    @login_required
    def get(self, company_id):
        company = GtiServiceCompany.query.filter_by(id=company_id).first_or_404()
        return service_company_schema.jsonify(company)

    @login_required
    def put(self, company_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        args = parser.parse_args()

        company = GtiServiceCompany.query.filter_by(id=company_id).first()
        # Изменения в объект вносятся внутри methods.edit, чтобы не перебирать их дважды
        methods.edit(editable_tbl=GtiServiceCompany, obj=company, args=args, user=current_user)

        return make_response(service_company_schema.jsonify(company), 201)


    @login_required
    def delete(self, company_id):
        company = GtiServiceCompany.query.filter_by(id=company_id).first()
        name = company.name
        args = dict()
        args['name'] = name
        # Изменения в объект вносятся внутри methods.edit, чтобы не перебирать их дважды
        methods.delete(editable_tbl=GtiServiceCompany, obj=company, args=args, user=current_user)
        return '', 204

class GtiServiceCompaniesApi(Resource):
    def get(self):
        companies = GtiServiceCompany.query.all()
        return service_companies_schema.jsonify(companies)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        args = parser.parse_args()

        if  args['name']:
            print(args['name'])
            company = GtiServiceCompany(name=args['name'])
            db.session.add(company)
            db.session.commit()

            methods.create(editable_tbl=GtiServiceCompany, obj=company, args=args, user=current_user)
            return service_company_schema.jsonify(company)
        else:
            return 'company is None', 400
