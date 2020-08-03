from flask_restful import Resource
from application.models.models import Customer
from .customer_full_data_schema import customer_full_data_schema, customers_full_data_schema

class CustomerFullDataApi(Resource):
    def get(self, customer_id):
        customer = Customer.query.filter_by(id=customer_id).first()
        return customer_full_data_schema.jsonify(customer)


class CustomersFullDataApi(Resource):
    def get(self):
        customers = Customer.query.all()
        return customers_full_data_schema.jsonify(customers)
