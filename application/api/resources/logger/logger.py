from application import ma, db
from application.models.logger import Logger, EditableField
from marshmallow import fields as ma_fields


class LoggerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Logger
        sqla_session = db.session
    editable_fields = ma_fields.Nested('LoggerEditableFieldSchema', default=[], many=True)


class LoggerEditableFieldSchema(ma.SQLAlchemyAutoSchema):
    id = ma_fields.Int()
    log_id = ma_fields.Int()
    __repr__ = ma.Str()


logger_schema = LoggerSchema()
loggers_schema = LoggerSchema(many=True)