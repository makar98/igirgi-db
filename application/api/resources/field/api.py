from flask_restful import Resource
from application.models.models import Field
from .field import field_schema, fields_schema
from flask_restful import reqparse
from application import db
from flask import make_response

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
        args = parser.parse_args()

        field = Field.query.filter_by(id=field_id).first()

        # Изменения в объект вносятся внутри methods.edit, чтобы не перебирать их дважды
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
        parser.add_argument('field')
        parser.add_argument('customer_id')
        args = parser.parse_args()

        if  args['field']:
            field = Field(name=args['field'], customer_id=int(args['customer_id']))
            db.session.add(field)
            db.session.commit()
            return field_schema.jsonify(field)
        else:
            return '', 400