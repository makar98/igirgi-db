from flask_restful import Resource
from application.models.gti.directory.chromatograph_type import GtiChromatographType
from .chromatograph_type import chromatograph_type_schema, chromatograph_types_schema
from flask_restful import reqparse
from application import db
from flask import make_response

from flask_security import login_required, current_user

from application.db_logger import methods

class GtiChromatographTypeApi(Resource):
    @login_required
    def get(self, chromatograph_type_id):
        chromatograph = GtiChromatographType.query.filter_by(id=chromatograph_type_id).first_or_404()
        return chromatograph_type_schema.jsonify(chromatograph)

    @login_required
    def put(self, chromatograph_type_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        args = parser.parse_args()

        chromatograph = GtiChromatographType.query.filter_by(id=chromatograph_type_id).first()
        # Изменения в объект вносятся внутри methods.edit, чтобы не перебирать их дважды
        methods.edit(editable_tbl=GtiChromatographType, obj=chromatograph, args=args, user=current_user)

        return make_response(chromatograph_type_schema.jsonify(chromatograph), 201)


    @login_required
    def delete(self, chromatograph_type_id):
        chromatograph = GtiChromatographType.query.filter_by(id=chromatograph_type_id).first()
        name = type.name
        args = dict()
        args['name'] = name
        # Изменения в объект вносятся внутри methods.edit, чтобы не перебирать их дважды
        methods.delete(editable_tbl=GtiChromatographType, obj=chromatograph, args=args, user=current_user)
        return  '', 204

class GtiChromatographTypesApi(Resource):
    def get(self):
        chromatographs = GtiChromatographType.query.all()
        return chromatograph_types_schema.jsonify(chromatographs)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        args = parser.parse_args()

        if  args['name']:
            chromatograph = GtiChromatographType(name=args['name'])
            db.session.add(chromatograph)
            db.session.commit()

            methods.create(editable_tbl=GtiChromatographType, obj=chromatograph, args=args, user=current_user)
            return chromatograph_type_schema.jsonify(chromatograph)
        else:
            return 'chromatograph is None', 400
