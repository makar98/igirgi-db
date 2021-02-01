from application import ma, db
from application.models.gti.table_row import GtiTableRow
from marshmallow import fields as ma_fields


class GtiTableRowTypeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = GtiTableRow
        sqla_session = db.session

table_row_schema = GtiTableRowTypeSchema()
table_rows_schema = GtiTableRowTypeSchema(many=True)