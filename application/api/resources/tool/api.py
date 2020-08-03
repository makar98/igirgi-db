from flask_restful import Resource
from application.models.models import Well
from application.models.models import Wellbore
from application.models.models import QualitySheet
from .tool import tool_schema, tools_schema
from flask_restful import reqparse
from application import db

class ToolApi(Resource):
    def get(self, tool_id):
        tool = Wellbore.query.filter_by(id=tool_id).first_or_404()
        return tool_schema.jsonify(tool)


class ToolsApi(Resource):
    def get(self):
        tools = Wellbore.query.all()
        return tools_schema.jsonify(tools)

    def post(self):
        return 'Метод не реализован', 400