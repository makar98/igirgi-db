from application import db
from sqlalchemy.orm import backref

from application.models.base.base_date import BaseDate


class QualitySheet(BaseDate):
    __human_name__ = 'Чек-лист ГИС'

    id = db.Column(db.Integer, primary_key=True)

    field_id = db.Column(db.Integer, db.ForeignKey('field.id'), nullable=False)
    pad_id = db.Column(db.Integer, db.ForeignKey('pad.id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    well_id = db.Column(db.Integer, db.ForeignKey('well.id'), nullable=False)
    well_type_id = db.Column(db.Integer, db.ForeignKey('well_type.id'), nullable=False)
    service_company_id = db.Column(db.Integer, db.ForeignKey('service_company.id'))
    wellbore_id = db.Column(db.Integer, db.ForeignKey('wellbore.id'), nullable=False)
    wellbore_type_id = db.Column(db.Integer, db.ForeignKey('wellbore_type.id'), nullable=False)

    section_interval_beg = db.Column(db.String(128))
    section_interval_end = db.Column(db.String(128))
    section_diameter = db.Column(db.String(128))

    methods = db.relationship('Method', backref=backref('QualitySheet'), lazy=True,
                                     cascade="all, delete, delete-orphan")

    information = db.Column(db.String(128))  # int???
    title_page = db.Column(db.String(128))
    construct = db.Column(db.String(128))
    column_size = db.Column(db.String(128))
    well_chronology = db.Column(db.String(128))
    drilling_fluid_info = db.Column(db.String(128))
    tool_composition = db.Column(db.String(128))
    depth_control_data = db.Column(db.String(128))
    directional_survey_data = db.Column(db.String(128))
    main_record = db.Column(db.String(128))
    data_processing_and_tool_parameters = db.Column(db.String(128))
    second_record = db.Column(db.String(128))
    curve_control_pad = db.Column(db.String(128))
    tool_calibration = db.Column(db.String(128))

    las_file_design = db.Column(db.String(128))  # int???
    las_file_design_well_section = db.Column(db.String(128))
    las_file_design_parameters_section = db.Column(db.String(128))
    las_file_design_curve_section = db.Column(db.String(128))

    incorrect_RT_data = db.Column(db.String(128))  # int???
    data_completeness = db.Column(db.String(128))
    data_transfer_settings = db.Column(db.String(128))
    curve_names = db.Column(db.String(128))
    mnemonic_description = db.Column(db.String(128))

    points_per_meter = db.Column(db.String(128))

    second_table_result = db.Column(db.String(128))

    grade = db.Column(db.Integer)


class Method(BaseDate):
    __human_name__ = 'Метод ГИС'

    id = db.Column(db.Integer, primary_key=True)

    check_list__id = db.Column(db.Integer, db.ForeignKey('quality_sheet.id'), nullable=False)

    method = db.Column(db.String(128))
    tool_type = db.Column(db.String(128))
    tool_num = db.Column(db.String(128))
    calibration_date = db.Column(db.String(128))
    gis_date = db.Column(db.String(128))
    receipt_date = db.Column(db.String(128))
    interval_beg = db.Column(db.String(128))
    interval_end = db.Column(db.String(128))
    rt_coefficient = db.Column(db.String(128))
    no_data_coefficient = db.Column(db.String(128))

    linkage_by_depth = db.Column(db.String(128))
    emissions = db.Column(db.String(128))
    noise = db.Column(db.String(128))
    check_measurement = db.Column(db.String(128))
    cross_plot_distribution = db.Column(db.String(128))
    tool_indication = db.Column(db.String(128))
    absolute_petrophysical_values = db.Column(db.String(128))
    notes = db.Column(db.String(2048))


class GisCurveCategory(BaseDate):
    __human_name__ = 'Категория кривой ГИС'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, unique=True)

    curves = db.relationship('GisCurve', backref=backref('gis_curve_category'), lazy=True,
                                     cascade="all, delete, delete-orphan")

    def __repr__(self):
        return self.name


class GisCurve(BaseDate):
    __human_name__ = 'Кривая ГИС'

    id = db.Column(db.Integer, primary_key=True)

    method = db.Column(db.String(128), nullable=False, unique=True)
    category_id = db.Column(db.Integer, db.ForeignKey('gis_curve_category.id'), nullable=False)

    latin = db.Column(db.String(128), nullable=False)
    curve_type = db.Column(db.String(128), nullable=False)
    units = db.Column(db.String(128), nullable=False)
    notes = db.Column(db.String(512), nullable=False)

    renames = db.relationship('GisCurveRename', backref=backref('gis_curve'), lazy=True,
                                     cascade="all, delete, delete-orphan")


class GisCurveRename(BaseDate):
    __human_name__ = 'Переименование кривых ГИС'
    __table_args__ = (
        db.UniqueConstraint('name', 'curve_id', name='unique_curve_rename'),
    )

    id = db.Column(db.Integer, primary_key=True)
    curve_id = db.Column(db.Integer, db.ForeignKey('gis_curve.id'), nullable=False)

    name = db.Column(db.String(128), nullable=False)
