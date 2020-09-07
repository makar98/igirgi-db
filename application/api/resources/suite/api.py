from flask_restful import Resource
from application.models.models import Suite, Field
from .suite import suite_schema, suites_schema
from flask_restful import reqparse
from application import db
from flask import make_response
import json

from flask_security import login_required, current_user

from application.db_logger import methods

class SuiteApi(Resource):
    @login_required
    def get(self, suite_id):
        suite = Suite.query.filter_by(id=suite_id).first_or_404()
        return suite_schema.jsonify(suite)

    @login_required
    def put(self, suite_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        parser.add_argument('fields_id')
        args = parser.parse_args()

        suite = Suite.query.filter_by(id=suite_id).first()

        args['fields_id'] = json.loads(args['fields_id'])

        args['fields'] = []
        if args['fields_id'] is not None:
            for field_id in args['fields_id']:
                args['fields'].append(Field.query.filter_by(id=field_id).first())
        del args['fields_id']

        # Изменения в объект вносятся внутри methods.edit, чтобы не перебирать их дважды
        methods.edit(editable_tbl=Suite, obj=suite, args=args, user=current_user)

        return make_response(suite_schema.jsonify(suite), 201)


    @login_required
    def delete(self, suite_id):
        suite = Suite.query.filter_by(id=suite_id).first()
        name = suite.name
        args = dict()
        args['name'] = name
        # Изменения в объект вносятся внутри methods.edit, чтобы не перебирать их дважды
        methods.delete(editable_tbl=Suite, obj=suite, args=args, user=current_user)
        return  '', 204

class SuitesApi(Resource):
    def get(self):
        suite = Suite.query.all()
        return suites_schema.jsonify(suite)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        parser.add_argument('fields_id')

        args = parser.parse_args()

        if  args['name']:
            suite = Suite(name=args['name'])
            db.session.add(suite)
            db.session.flush()

            for field_id in json.loads(args['fields_id']):
                print(field_id)
                field = Field.query.filter_by(id=int(field_id)).first()
                field.suites.append(suite)
            db.session.commit()

            methods.create(editable_tbl=Suite, obj=suite, args=args, user=current_user)
            return suite_schema.jsonify(suite)
        else:
            return 'parameter is None', 400
