from flask_restful import Resource
from application.models.gti.format import GtiFormat
from .format import format_schema, formats_schema
from flask_restful import reqparse
from application import db
from flask import make_response

from flask_security import login_required, current_user

from application.db_logger import methods

class GtiFormatApi(Resource):
    @login_required
    def get(self, gri_format_id):
        gti_format = GtiFormat.query.filter_by(id=gri_format_id).first_or_404()
        return format_schema.jsonify(gti_format)

    @login_required
    def put(self, gti_format_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        args = parser.parse_args()

        gti_format = GtiFormat.query.filter_by(id=gti_format_id).first()
        # Изменения в объект вносятся внутри methods.edit, чтобы не перебирать их дважды
        methods.edit(editable_tbl=GtiFormat, obj=gti_format, args=args, user=current_user)

        return make_response(format_schema.jsonify(gti_format), 201)


    @login_required
    def delete(self, gti_format_id):
        gti_format = GtiFormat.query.filter_by(id=gti_format_id).first()
        name = gti_format.name
        args = dict()
        args['name'] = name
        # Изменения в объект вносятся внутри methods.edit, чтобы не перебирать их дважды
        methods.delete(editable_tbl=GtiFormat, obj=gti_format, args=args, user=current_user)
        return  '', 204

class GtiFormatsApi(Resource):
    def get(self):
        gti_formats = GtiFormat.query.all()
        return formats_schema.jsonify(gti_formats)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        parser.add_argument('parameter_id')
        args = parser.parse_args()

        if  args['name']:
            gti_format = GtiFormat(name=args['name'], parameter_id=args['parameter_id'])
            db.session.add(gti_format)
            db.session.commit()

            methods.create(editable_tbl=GtiFormat, obj=gti_format, args=args, user=current_user)
            return format_schema.jsonify(gti_format)
        else:
            return 'gti_format is None', 400
