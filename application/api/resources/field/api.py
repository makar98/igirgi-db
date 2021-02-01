from flask_restful import Resource
from application.models.models import Field, Suite
from .field import field_schema, fields_schema
from flask_restful import reqparse
from application import db
from flask import make_response
import json

from flask_security import login_required, current_user
from application.db_logger import methods

class FieldApi(Resource):
    def get(self, field_id):
        field = Field.query.filter_by(id=field_id).first_or_404()
        return field_schema.jsonify(field)

    @login_required
    def put(self, field_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        parser.add_argument('suites_id')
        args = parser.parse_args()

        field = Field.query.filter_by(id=field_id).first()

        # Изменения в объект вносятся внутри methods.edit, чтобы не перебирать их дважды
        args['suites_id'] = json.loads(args['suites_id'])
        # print(args)
        args['suites'] = [] # Нахуя это делается? Надо разобраться!
        # print(args)
        if args['suites_id'] is not None:
            for suite_id in args['suites_id']:
                args['suites'].append(Suite.query.filter_by(id=suite_id).first())
        del args['suites_id']
        methods.edit(editable_tbl=Field, obj=field, args=args, user=current_user)

        return make_response(field_schema.jsonify(field), 201)

    @login_required
    def delete(self, field_id):
        field = Field.query.filter_by(id=field_id).first()
        name = field.name
        args = dict()
        args['name'] = name
        # Изменения в объект вносятся внутри methods.edit, чтобы не перебирать их дважды
        methods.delete(editable_tbl=Field, obj=field, args=args, user=current_user)
        return '', 204

class FieldsApi(Resource):
    def get(self):
        fields = Field.query.all()
        return fields_schema.jsonify(fields)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        parser.add_argument('customer_id')
        args = parser.parse_args()

        if  args['name']:
            field = Field(name=args['name'], customer_id=int(args['customer_id']))
            db.session.add(field)
            db.session.commit()

            methods.create(editable_tbl=Field, obj=field, args=args, user=current_user)
            return field_schema.jsonify(field)
        else:
            return '', 400