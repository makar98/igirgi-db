from application import ma, db
from marshmallow import fields as ma_fields

from application.models.models import Layer


class LayerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Layer
        sqla_session = db.session


layer_schema = LayerSchema()
layers_schema = LayerSchema(many=True)