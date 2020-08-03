from application import db
from datetime import datetime
from sqlalchemy.orm import backref
from .user import User

"""
    !!! flask db stamp head
    !!! flask db migrate
    !!! flask db upgrade


    if
        flask db heads ! =flask db current:
            flask db stamp head

    Если не находит версию
    DELETE FROM alembic_version WHERE version_num='3aae6532b560';
"""


class Customer(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, unique=True)
    fields = db.relationship('Field', backref=backref('customer'), lazy=True)
    emails = db.relationship('CustomerEmail', backref=backref('customer'), lazy=True)
    wells = db.relationship('Well', backref=backref('customer'), lazy=True)

    def __repr__(self):
        return self.name


class Field(db.Model):
    __table_args__ = (
        db.UniqueConstraint('customer_id', 'name', name='unique_field'),
    )
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    date_add = db.Column(db.DateTime, default=datetime.utcnow)
    suites = db.relationship('Suite', backref=backref('field'), lazy=True)
    pads = db.relationship('Pad', backref=backref('field'), lazy=True)
    wells = db.relationship('Well', backref=backref('field'), lazy=True)

    quality_sheets = db.relationship('QualitySheet', backref=backref('field'), lazy=True)


    def __repr__(self):
        return self.name


class Pad(db.Model):
    __table_args__ = (
        db.UniqueConstraint('name', 'field_id', name='unique_pad'),
    )
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    field_id = db.Column(db.Integer, db.ForeignKey('field.id'), nullable=False)
    date_add = db.Column(db.DateTime, default=datetime.utcnow)
    wells = db.relationship('Well', backref=backref('pad'), lazy=True)

    quality_sheets = db.relationship('QualitySheet', backref=backref('pad'), lazy=True)

    def __repr__(self):
        return self.name


class Well(db.Model):
    __table_args__ = (
        db.UniqueConstraint('name', 'field_id', 'pad_id', 'customer_id', name='unique_well'),
    )
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    well_type_id = db.Column(db.Integer, db.ForeignKey('well_type.id'), nullable=False)

    wellbores = db.relationship('Wellbore', backref=backref('well'), cascade='all, delete-orphan', lazy=True)

    create_date = db.Column(db.DateTime, default=datetime.utcnow)
    change_date = db.Column(db.DateTime)

    field_id = db.Column(db.Integer, db.ForeignKey('field.id'), nullable=False)
    pad_id = db.Column(db.Integer, db.ForeignKey('pad.id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)

    quality_sheets = db.relationship('QualitySheet', backref=backref('well'), lazy=True)


    def __repr__(self):
        return f'Заказзчик: {self.customer}. Месторождение: {self.field}. Скважина: {self.name}'


class WellType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)

    create_date = db.Column(db.DateTime, default=datetime.utcnow)
    change_date = db.Column(db.DateTime)

    well = db.relationship('Well', uselist=False, backref=backref('well_type'),
                                cascade='all, delete-orphan', lazy=True)

    quality_sheets = db.relationship('QualitySheet', backref=backref('well_type'), lazy=True)

    def __repr__(self):
        return self.name


class Wellbore(db.Model):
    __table_args__ = (
        db.UniqueConstraint('name', 'wellbore_type_id', 'well_id', name='unique_wellbore_type'),
    )
    id = db.Column(db.Integer, primary_key=True)

    create_date = db.Column(db.DateTime, default=datetime.utcnow)
    change_date = db.Column(db.DateTime)

    name = db.Column(db.String(128), nullable=False)
    wellbore_type_id = db.Column(db.Integer, db.ForeignKey('wellbore_type.id'), nullable=False)
    well_id = db.Column(db.Integer, db.ForeignKey('well.id'), nullable=False)

    is_gis = db.Column(db.Boolean, default=False)
    is_gti = db.Column(db.Boolean, default=False)

    quality_sheets = db.relationship('QualitySheet', backref=backref('wellbore'), lazy=True)

    gti_row = db.relationship('GtiTableRow', backref=backref('wellbore'), uselist=False, lazy=True)


    def __repr__(self):
        return self.name


class WellboreType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)

    create_date = db.Column(db.DateTime, default=datetime.utcnow)
    change_date = db.Column(db.DateTime)

    wellbore = db.relationship('Wellbore', uselist=False, backref=backref('wellbore_type'),
                                cascade='all, delete-orphan', lazy=True)

    quality_sheets = db.relationship('QualitySheet', backref=backref('wellbore_type'), lazy=True)

    def __repr__(self):
        return self.name


class Suite(db.Model):
    __table_args__ = (
        db.UniqueConstraint('name', 'field_id', name='unique_suite'),
    )
    id = db.Column(db.Integer, primary_key=True)

    create_date = db.Column(db.DateTime, default=datetime.utcnow)
    change_date = db.Column(db.DateTime)

    name = db.Column(db.String(64), nullable=False)
    field_id = db.Column(db.Integer, db.ForeignKey('field.id'), nullable=False)
    layers = db.relationship('Layer', backref=backref('suite'), lazy=True)

    def __repr__(self):
        return self.name


class Layer(db.Model):
    __table_args__ = (
        db.UniqueConstraint('name', 'suite_id', name='unique_layer'),
    )
    id = db.Column(db.Integer, primary_key=True)

    create_date = db.Column(db.DateTime, default=datetime.utcnow)
    change_date = db.Column(db.DateTime)

    name = db.Column(db.String(64), nullable=False)
    suite_id = db.Column(db.Integer, db.ForeignKey('suite.id'), nullable=False)
    path_to_files = db.relationship('FilePath', backref=backref('layer'), lazy=True)

    def __repr__(self):
        return self.name


class CompanyEmail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('service_company.id'), nullable=False)

    def __repr__(self):
        return self.email


class CustomerEmail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)

    def __repr__(self):
        return self.email


class FilePath(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(256), nullable=False)
    layer_id = db.Column(db.Integer, db.ForeignKey('layer.id'), nullable=False)

    def __repr__(self):
        return self.path.split('\\')[-1]


class ServiceCompany(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    quality_sheets = db.relationship('QualitySheet', backref=backref('service_company'), lazy=True)
    tools = db.relationship('Tool', backref=backref('service_company'), lazy=True)
    emails = db.relationship('CompanyEmail', backref=backref('service_company'), lazy=True)


    def __repr__(self):
        return self.name


class Tool(db.Model):
    __tablename__ = 'tool'
    tool_type = db.Column(db.String(128))
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('service_company.id'), nullable=False)

    # is_overdue = db.Column(db.Bool)

    def __repr__(self):
        return self.name


class QualitySheet(db.Model):
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

    methods = db.relationship('Method', backref=backref('QualitySheet'), lazy=True)

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


class Method(db.Model):
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


# GIS
class GisCurveCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, unique=True)

    curves = db.relationship('GisCurve', backref=backref('gis_curve_category'), lazy=True)

    def __repr__(self):
        return self.name


class GisCurve(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    date_add = db.Column(db.DateTime, default=datetime.utcnow)

    method = db.Column(db.String(128), nullable=False, unique=True)
    category_id = db.Column(db.Integer, db.ForeignKey('gis_curve_category.id'), nullable=False)

    latin = db.Column(db.String(128), nullable=False)
    curve_type = db.Column(db.String(128), nullable=False)
    units = db.Column(db.String(128), nullable=False)
    notes = db.Column(db.String(512), nullable=False)

    renames = db.relationship('GisCurveRename', backref=backref('gis_curve'), lazy=True)


class GisCurveRename(db.Model):
    __table_args__ = (
        db.UniqueConstraint('name', 'curve_id', name='unique_curve_rename'),
    )
    id = db.Column(db.Integer, primary_key=True)
    curve_id = db.Column(db.Integer, db.ForeignKey('gis_curve.id'), nullable=False)

    date_add = db.Column(db.DateTime, default=datetime.utcnow)

    name = db.Column(db.String(128), nullable=False)


# GTI
author_gti_row = db.Table('author_gti',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('table_row_id', db.Integer, db.ForeignKey('gti_table_row.id'))
)


class GtiTableRow(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    date_add = db.Column(db.DateTime, default=datetime.utcnow)

    wellbore_id = db.Column(db.Integer, db.ForeignKey('wellbore.id'), nullable=False)

    layer = db.Column(db.String(128)) #  Сделать связь к модели Layer
    company = db.Column(db.String(128)) #  Сделать связь к модели GtiServiceCompany
    efficiency = db.Column(db.String(128))
    mud_gas_quality =db.Column(db.String(128))
    frequency = db.Column(db.Integer, default=0)
    bottom_hole_plus_igti = db.Column(db.String(128))
    bottom_hole = db.Column(db.String(128))

    authors = db.relationship('User', secondary=author_gti_row, backref='authors')

    degasser = db.Column(db.String(128))
    notes = db.Column(db.String(512))

    gti_quality_sheet = db.relationship('GtiQualitySheet', backref=backref('gti_table_row'), uselist=False, lazy=True)


class GtiQualitySheet(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    date_add = db.Column(db.DateTime, default=datetime.utcnow)

    gti_table_row_id = db.Column(db.Integer, db.ForeignKey('gti_table_row.id'), nullable=False)


class GtiTechnologicalResearch(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    date_add = db.Column(db.DateTime, default=datetime.utcnow)

    interval_beg = db.Column(db.Integer)
    interval_end = db.Column(db.Integer)

    date = db.Column(db.DateTime, default=datetime.utcnow)
    parameter = db.Column(db.String(128))
    format = db.Column(db.String(128))
    falsification = db.Column(db.String(128))


class GtiGasResearch(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    date_add = db.Column(db.DateTime, default=datetime.utcnow)

    interval_beg = db.Column(db.Integer)
    interval_end = db.Column(db.Integer)

    date = db.Column(db.DateTime, default=datetime.utcnow)
    parameter = db.Column(db.String(128))
    format = db.Column(db.String(128))
    falsification = db.Column(db.String(128))


class GtiGeoResearch(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    date_add = db.Column(db.DateTime, default=datetime.utcnow)

    interval_beg = db.Column(db.Integer)
    interval_end = db.Column(db.Integer)

    date = db.Column(db.DateTime, default=datetime.utcnow)
    parameter = db.Column(db.String(128))
    format = db.Column(db.String(128))
    falsification = db.Column(db.String(128))
