from application import ma, db
from application.models.models import  Tool
from marshmallow import fields as ma_fields


class ToolSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Tool
        sqla_session = db.session




tool_schema = ToolSchema()
tools_schema = ToolSchema(many=True)