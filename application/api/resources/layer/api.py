from flask_restful import Resource
from application.models.models import Layer
from .layer import layer_schema, layers_schema
from flask_restful import reqparse
from application import db
from flask import make_response

from flask_security import login_required, current_user

from application.db_logger import methods

class LayerApi(Resource):
    @login_required
    def get(self, layer_id):
        layer = Layer.query.filter_by(id=layer_id).first_or_404()
        return layer_schema.jsonify(layer)

    @login_required
    def put(self, layer_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        args = parser.parse_args()

        layer = Layer.query.filter_by(id=layer_id).first()
        # Изменения в объект вносятся внутри methods.edit, чтобы не перебирать их дважды
        methods.edit(editable_tbl=Layer, obj=layer, args=args, user=current_user)

        return make_response(layer_schema.jsonify(layer), 201)


    @login_required
    def delete(self, layer_id):
        layer = Layer.query.filter_by(id=layer_id).first()
        name = layer.name
        args = dict()
        args['name'] = name
        # Изменения в объект вносятся внутри methods.edit, чтобы не перебирать их дважды
        methods.delete(editable_tbl=Layer, obj=layer, args=args, user=current_user)
        return  '', 204

class LayersApi(Resource):
    def get(self):
        layers = Layer.query.all()
        return layers_schema.jsonify(layers)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        parser.add_argument('suite_id')
        args = parser.parse_args()

        if  args['name']:
            print(args['name'])
            layer = Layer(name=args['name'], suite_id=args['suite_id'])
            db.session.add(layer)
            db.session.commit()

            methods.create(editable_tbl=Layer, obj=layer, args=args, user=current_user)
            return layer_schema.jsonify(layer)
        else:
            return 'parameter is None', 400
