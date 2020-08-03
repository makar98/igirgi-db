from flask_restful import Resource
from application.models.models import QualitySheet
from .quality_sheet import quality_sheet_schema, quality_sheets_schema
from flask_restful import reqparse
from application import db

class QualitySheetApi(Resource):
    def get(self, quality_sheet_id):
        quality_sheet = QualitySheet.query.filter_by(id=quality_sheet_id).first_or_404()
        return quality_sheet_schema.jsonify(quality_sheet)


class QualitySheetsApi(Resource):
    def get(self):
        quality_sheets = QualitySheet.query.all()
        return quality_sheets_schema.jsonify(quality_sheets)

    def post(self):
        parser = reqparse.RequestParser()

        for attr in dir(QualitySheet):
            if not attr.startswith('_'):
                parser.add_argument(attr)

        args = parser.parse_args()

        if  args:
            print(args)
            quality_sheet = QualitySheet(field_id=int(args['field_id']), pad_id=int(args['pad_id']),
                                         customer_id=int(args['customer_id']), well_id=int(args['well_id']),
                                         well_type_id=int(args['well_type_id']), wellbore_id=int(args['wellbore_id']),
                                         wellbore_type_id=int(args['wellbore_type_id']),
                                         service_company_id=int(args['service_company_id']),
                                         section_interval_beg=args['section_interval_beg'],
                                         section_interval_end=args['section_interval_end'],
                                         section_diameter=args['section_diameter'],
                                         information=args['information'],
                                         title_page=args['title_page'], construct=args['construct'],
                                         column_size=args['column_size'], well_chronology=args['well_chronology'],
                                         drilling_fluid_info=args['drilling_fluid_info'],
                                         tool_composition=args['tool_composition'],
                                         depth_control_data=args['depth_control_data'],
                                         directional_survey_data=args['directional_survey_data'],
                                         main_record=args['main_record'],
                                         data_processing_and_tool_parameters=args['data_processing_and_tool_parameters'],
                                         second_record=args['second_record'],
                                         curve_control_pad=args['curve_control_pad'],
                                         tool_calibration=args['tool_calibration'],
                                         las_file_design=args['las_file_design'],
                                         las_file_design_well_section=args['las_file_design_well_section'],
                                         las_file_design_parameters_section=args['las_file_design_parameters_section'],
                                         las_file_design_curve_section=args['las_file_design_curve_section'],
                                         incorrect_RT_data=args['incorrect_RT_data'],
                                         data_completeness=args['data_completeness'],
                                         data_transfer_settings=args['data_transfer_settings'],
                                         curve_names=args['curve_names'],
                                         mnemonic_description=args['mnemonic_description'],
                                         points_per_meter=args['points_per_meter'],
                                         second_table_result=args['second_table_result'],
                                         grade=int(args['grade']))
            db.session.add(quality_sheet)
            db.session.commit()
            print(args['methods'])
            return quality_sheet_schema.jsonify(quality_sheet)
        else:
            return '', 400