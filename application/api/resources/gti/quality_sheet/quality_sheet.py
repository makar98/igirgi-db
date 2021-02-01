from application import ma, db
from application.models.gti.quality_sheet.quality_sheet import GtiQualitySheet
from application.models.gti.quality_sheet.row import GtiGeoResearch, GtiGasResearch, GtiTechnologicalResearch

from marshmallow import fields as ma_fields


class QualitySheetSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = GtiQualitySheet
        sqla_session = db.session
    #rows_technological = ma_fields.Nested('SheetTechSchema', default=[], many=True)
    gti_table_row_id = ma_fields.Int()
    rows_technological = ma_fields.Nested('SheetTechSchema', default=[], many=True)
    rows_gas = ma_fields.Nested('SheetGasSchema', default=[], many=True)
    rows_geo = ma_fields.Nested('SheetGeoSchema', default=[], many=True)

class SheetTechSchema(ma.SQLAlchemyAutoSchema):
    id = ma_fields.Int()
    date = ma_fields.DateTime()
    parameter_id = ma_fields.Int()
    format_id = ma_fields.Int()

class SheetGasSchema(ma.SQLAlchemyAutoSchema):
    id = ma_fields.Int()
    date = ma_fields.DateTime()
    parameter_id = ma_fields.Int()
    format_id = ma_fields.Int()

class SheetGeoSchema(ma.SQLAlchemyAutoSchema):
    id = ma_fields.Int()
    date = ma_fields.DateTime()
    parameter_id = ma_fields.Int()
    format_id = ma_fields.Int()




quality_sheet_schema = QualitySheetSchema()
quality_sheets_schema = QualitySheetSchema(many=True)