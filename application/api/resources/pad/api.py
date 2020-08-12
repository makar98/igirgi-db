from flask_restful import Resource
from application.models.models import Pad
from .pad import pad_schema, pads_schema
from flask_restful import reqparse
from application import db
from flask import make_response

from flask_security import login_required, current_user
from application.db_logger import methods

class PadApi(Resource):
    def get(self, pad_id):
        pad = Pad.query.filter_by(id=pad_id).first_or_404()
        return pad_schema.jsonify(pad)

    @login_required
    def put(self, pad_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        args = parser.parse_args()
        if args['name']:
            pad = Pad.query.filter_by(id=pad_id).first()
            print(pad)

            methods.edit(editable_tbl=Pad, obj=pad, args=args, user=current_user)
            return make_response(pad_schema.jsonify(pad), 201)
        else:
            return '', 404

    @login_required
    def delete(self, pad_id):
        pad = Pad.query.filter_by(id=pad_id).first()
        name = pad.name
        args = dict()
        args['name'] = name
        # Изменения в объект вносятся внутри methods.edit, чтобы не перебирать их дважды
        methods.delete(editable_tbl=Pad, obj=pad, args=args, user=current_user)
        return '', 204

class PadsApi(Resource):
    def get(self):
        pads = Pad.query.all()
        return pads_schema.jsonify(pads)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('pad')
        parser.add_argument('field_id')
        args = parser.parse_args()
        print(args)
        if  args['pad'] and args['field_id']:
            pad = Pad(name=args['pad'], field_id=int(args['field_id']))
            db.session.add(pad)
            db.session.commit()

            methods.create(editable_tbl=Pad, obj=pad, args=args, user=current_user)
            return pad_schema.jsonify(pad)
        else:
            return '', 400