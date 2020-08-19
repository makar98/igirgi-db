from flask_restful import Resource
from application.models.gti.parameter import GtiParameter
from application.models.gti.format import GtiFormat
from .parameter import parameter_schema, parameters_schema
from flask_restful import reqparse
from application import db
from flask import make_response

from flask_security import login_required, current_user

from application.db_logger import methods

class GtiParameterApi(Resource):
    @login_required
    def get(self, parameter_id):
        parameter = GtiParameter.query.filter_by(id=parameter_id).first_or_404()
        return parameter_schema.jsonify(parameter)

    @login_required
    def put(self, parameter_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        args = parser.parse_args()

        parameter = GtiParameter.query.filter_by(id=parameter_id).first()
        # Изменения в объект вносятся внутри methods.edit, чтобы не перебирать их дважды
        methods.edit(editable_tbl=GtiParameter, obj=parameter, args=args, user=current_user)

        return make_response(parameter_schema.jsonify(parameter), 201)


    @login_required
    def delete(self, parameter_id):
        parameter = GtiParameter.query.filter_by(id=parameter_id).first()
        name = parameter.name
        args = dict()
        args['name'] = name
        # Изменения в объект вносятся внутри methods.edit, чтобы не перебирать их дважды
        methods.delete(editable_tbl=GtiParameter, obj=parameter, args=args, user=current_user)
        return  '', 204

class GtiParametersApi(Resource):
    def get(self):
        parameters = GtiParameter.query.all()
        return parameters_schema.jsonify(parameters)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        args = parser.parse_args()

        if  args['name']:
            print(args['name'])
            parameter = GtiParameter(name=args['name'])
            db.session.add(parameter)
            db.session.commit()

            methods.create(editable_tbl=GtiParameter, obj=parameter, args=args, user=current_user)
            return parameter_schema.jsonify(parameter)
        else:
            return 'parameter is None', 400
