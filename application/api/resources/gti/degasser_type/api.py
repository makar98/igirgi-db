from flask_restful import Resource
from application.models.gti.directory.degasser_type import GtiDegasserType
from .degasser_type import degasser_type_schema, degasser_types_schema
from flask_restful import reqparse
from application import db
from flask import make_response

from flask_security import login_required, current_user

from application.db_logger import methods

class GtiDegasserApi(Resource):
    @login_required
    def get(self, degasser_type_id):
        degasser = GtiDegasserType.query.filter_by(id=degasser_type_id).first_or_404()
        return degasser_type_schema.jsonify(degasser)

    @login_required
    def put(self, degasser_type_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        args = parser.parse_args()

        degasser = GtiDegasserType.query.filter_by(id=degasser_type_id).first()
        # Изменения в объект вносятся внутри methods.edit, чтобы не перебирать их дважды
        methods.edit(editable_tbl=GtiDegasserType, obj=degasser, args=args, user=current_user)

        return make_response(degasser_type_schema.jsonify(degasser), 201)


    @login_required
    def delete(self, degasser_type_id):
        degasser = GtiDegasserType.query.filter_by(id=degasser_type_id).first()
        name = degasser.name
        args = dict()
        args['name'] = name
        # Изменения в объект вносятся внутри methods.edit, чтобы не перебирать их дважды
        methods.delete(editable_tbl=GtiDegasserType, obj=degasser, args=args, user=current_user)
        return  '', 204

class GtiDegassersApi(Resource):
    def get(self):
        degassers = GtiDegasserType.query.all()
        return degasser_types_schema.jsonify(degassers)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        args = parser.parse_args()

        if  args['name']:
            print(args['name'])
            degasser = GtiDegasserType(name=args['name'])
            db.session.add(degasser)
            db.session.commit()

            methods.create(editable_tbl=GtiDegasserType, obj=degasser, args=args, user=current_user)
            return degasser_type_schema.jsonify(degasser)
        else:
            return 'degasser is None', 400
