from flask_restful import Resource
from application.models.models import Pad
from .pad import pad_schema, pads_schema
from flask_restful import reqparse
from application import db


from flask_security import login_required
from application.db_logger.methods import edit

class PadApi(Resource):
    def get(self, pad_id):
        pad = Pad.query.filter_by(id=pad_id).first_or_404()
        return pad_schema.jsonify(pad)

    @login_required
    def put(self, pad_id):
        parser = reqparse.RequestParser()
        parser.add_argument('pad')
        parser.add_argument('field_id')
        args = parser.parse_args()

        pad = Pad.query.filter_by(id=pad_id).first()

        edit(editable_tbl=Pad, obj=pad, args=args)

        return '', 201

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
            return pad_schema.jsonify(pad)
        else:
            return '', 400