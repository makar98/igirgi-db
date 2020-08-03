from flask_restful import Resource
from application.models.models import Customer
from .customer import customer_schema, customers_schema
from flask_restful import reqparse
from application import db
from flask import make_response

from flask_security import login_required, current_user

from application.db_logger import methods

class CustomerApi(Resource):
    @login_required
    def get(self, customer_id):
        customer = Customer.query.filter_by(id=customer_id).first_or_404()
        return customer_schema.jsonify(customer)

    @login_required
    def put(self, customer_id):

        parser = reqparse.RequestParser()
        parser.add_argument('name')
        args = parser.parse_args()

        customer = Customer.query.filter_by(id=customer_id).first()
        # Изменения в объект вносятся внутри methods.edit, чтобы не перебирать их дважды
        methods.edit(editable_tbl=Customer, obj=customer, args=args, user=current_user)

        return make_response(customer_schema.jsonify(customer), 201)

    @login_required
    def delete(self, customer_id):
        customer = Customer.query.filter_by(id=customer_id).first()
        name = customer.name
        args = dict()
        args['name'] = name
        # Изменения в объект вносятся внутри methods.edit, чтобы не перебирать их дважды
        methods.delete(editable_tbl=Customer, obj=customer, args=args, user=current_user)
        return  '', 204

class CustomersApi(Resource):
    def get(self):
        customers = Customer.query.all()
        return customers_schema.jsonify(customers)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('customer')
        args = parser.parse_args()

        if  args['customer']:
            print(args['customer'])
            customer = Customer(name=args['customer'])
            db.session.add(customer)
            db.session.commit()

            methods.create(editable_tbl=Customer, obj=customer, args=args, user=current_user)
            return customer_schema.jsonify(customer)
        else:
            return 'customer is None', 400



