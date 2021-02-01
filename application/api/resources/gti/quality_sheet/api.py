from flask_restful import Resource, reqparse
from flask import make_response

from .quality_sheet import quality_sheet_schema, quality_sheets_schema
from application.models.gti.quality_sheet.quality_sheet import GtiQualitySheet
from application.models.gti.quality_sheet.row import GtiGeoResearch, GtiGasResearch, GtiTechnologicalResearch
from application import db

from flask_security import login_required, current_user

from application.db_logger import methods

def row_update(row, *args, **kwargs):
    for arg in args:
        pass



class GtiQualitySheetApi(Resource):
    @login_required
    def get(self, quality_sheet_id):
        quality_sheet = GtiQualitySheet.query.filter_by(id=quality_sheet_id).first_or_404()
        return quality_sheet_schema.jsonify(quality_sheet)

    # Тут только добавлять/удалять строки в исследованиях
    @login_required
    def put(self, quality_sheet_id):
        parser = reqparse.RequestParser()
        parser.add_argument('rows_tech')
        parser.add_argument('rows_gas')
        parser.add_argument('rows_geo')
        args = parser.parse_args()

        sheet = GtiQualitySheet.query.filter_by(id=quality_sheet_id).first()

        for row in args['row_tech']:
            db_row = GtiTechnologicalResearch.query.filter_by(id=row['id']).first()

            # Скорее всего будет хуйня, если в sheet.rows_technological будет что-то типа None.
            # Такое вообще возможно?
            if db_row in sheet.rows_technological:
                row_update(db_row, )
            else:
                new_row = GtiTechnologicalResearch(interval_beg=row['interval_beg'],
                                                   interval_end=row['interval_end'],
                                                   parameter_id=row['parameter_id'],
                                                   format_id=row['format_id'],
                                                   )
                db.sesion.add(new_row)
        return make_response('', 201)
