from application import ma, db
from application.models.gis import QualitySheet
from marshmallow import fields as ma_fields


class QualitySheet(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = QualitySheet
        sqla_session = db.session


quality_sheet_schema = QualitySheet()
quality_sheets_schema = QualitySheet(many=True)