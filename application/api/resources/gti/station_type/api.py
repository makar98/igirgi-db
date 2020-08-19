from flask_restful import Resource
from application.models.gti.directory.station_type import GtiStationType
from .station_type import station_type_schema, station_types_schema
from flask_restful import reqparse
from application import db
from flask import make_response

from flask_security import login_required, current_user

from application.db_logger import methods

class GtiStationTypeApi(Resource):
    @login_required
    def get(self, station_type_id):
        station_type = GtiStationType.query.filter_by(id=station_type_id).first_or_404()
        return station_type_schema.jsonify(station_type)

    @login_required
    def put(self, station_type_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        args = parser.parse_args()

        station_type = GtiStationType.query.filter_by(id=station_type_id).first()
        # Изменения в объект вносятся внутри methods.edit, чтобы не перебирать их дважды
        methods.edit(editable_tbl=GtiStationType, obj=station_type, args=args, user=current_user)

        return make_response(station_type_schema.jsonify(station_type), 201)


    @login_required
    def delete(self, station_type_id):
        station_type = GtiStationType.query.filter_by(id=station_type_id).first()
        name = station_type.name
        args = dict()
        args['name'] = name
        # Изменения в объект вносятся внутри methods.edit, чтобы не перебирать их дважды
        methods.delete(editable_tbl=GtiStationType, obj=station_type, args=args, user=current_user)
        return '', 204

class GtiStationTypesApi(Resource):
    def get(self):
        station_types = GtiStationType.query.all()
        return station_types_schema.jsonify(station_types)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        args = parser.parse_args()

        if  args['name']:
            station_type = GtiStationType(name=args['name'])
            db.session.add(station_type)
            db.session.commit()

            methods.create(editable_tbl=GtiStationType, obj=station_type, args=args, user=current_user)
            return station_type_schema.jsonify(station_type)
        else:
            return 'company is None', 400
