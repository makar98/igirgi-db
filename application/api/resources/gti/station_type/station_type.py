from application import ma, db
from application.models.gti.directory.station_type import GtiStationType
from marshmallow import fields as ma_fields


class GtiStationTypeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = GtiStationType
        sqla_session = db.session
    gti_rows = ma_fields.Nested('GtiTableRowStationTypeSchema', default=[], many=True)


class GtiTableRowStationTypeSchema(ma.SQLAlchemyAutoSchema):
    id = ma_fields.Int()
    station_type_id = ma_fields.Int()
    wellbore_id = ma_fields.Int()


station_type_schema = GtiStationTypeSchema()
station_types_schema = GtiStationTypeSchema(many=True)