from application import db
from datetime import datetime
from sqlalchemy.orm import backref
from .base.base_date import BaseDate
from .gti.format import GtiFormat
from .gti.table_row import GtiTableRow
from .gis import GisCurveRename, GisCurveCategory, GisCurve

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


class Customer(BaseDate):
    __human_name__ = 'Заказчик'

    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, unique=True)
    fields = db.relationship('Field', backref=backref('customer'), lazy=True,
                                     cascade="all, delete, delete-orphan")
    emails = db.relationship('CustomerEmail', backref=backref('customer'), lazy=True,
                                     cascade="all, delete, delete-orphan")
    wells = db.relationship('Well', backref=backref('customer'), lazy=True,
                                     cascade="all, delete, delete-orphan")
    quality_sheets = db.relationship('QualitySheet', backref=backref('customer'), lazy=True,
                                     cascade="all, delete, delete-orphan")

    def __repr__(self):
        return self.name


class Field(BaseDate):
    __human_name__ = 'Месторождение'

    __table_args__ = (
        db.UniqueConstraint('customer_id', 'name', name='unique_field'),
    )
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    date_add = db.Column(db.DateTime, default=datetime.utcnow)

    suites = db.relationship('Suite', backref=backref('field'), lazy=True,
                                     cascade="all, delete, delete-orphan")
    pads = db.relationship('Pad', backref=backref('field'), lazy=True,
                                     cascade="all, delete, delete-orphan")
    wells = db.relationship('Well', backref=backref('field'), lazy=True,
                                     cascade="all, delete, delete-orphan")

    quality_sheets = db.relationship('QualitySheet', backref=backref('field'), lazy=True)


    def __repr__(self):
        return self.name


class Pad(BaseDate):
    __human_name__ = 'Куст'

    __table_args__ = (
        db.UniqueConstraint('name', 'field_id', name='unique_pad'),
    )
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    field_id = db.Column(db.Integer, db.ForeignKey('field.id'), nullable=False)

    wells = db.relationship('Well', backref=backref('pad'), lazy=True,
                            cascade="all, delete, delete-orphan")

    quality_sheets = db.relationship('QualitySheet', backref=backref('pad'), lazy=True,
                                     cascade="all, delete, delete-orphan")

    def __repr__(self):
        return self.name


class Well(BaseDate):
    __human_name__ = 'Скважина'

    __table_args__ = (
        db.UniqueConstraint('name', 'field_id', 'pad_id', 'customer_id', name='unique_well'),
    )
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    well_type_id = db.Column(db.Integer, db.ForeignKey('well_type.id'), nullable=False)

    wellbores = db.relationship('Wellbore', backref=backref('well'),
                                cascade='all, delete, delete-orphan', lazy=True)


    field_id = db.Column(db.Integer, db.ForeignKey('field.id'), nullable=False)
    pad_id = db.Column(db.Integer, db.ForeignKey('pad.id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)

    quality_sheets = db.relationship('QualitySheet', backref=backref('well'), lazy=True,
                                     cascade="all, delete, delete-orphan")


    def __repr__(self):
        return f'Заказзчик: {self.customer}. Месторождение: {self.field}. Скважина: {self.name}'


class WellType(BaseDate):
    __human_name__ = 'Тип скважины'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)

    well = db.relationship('Well', uselist=False, backref=backref('well_type'),
                                cascade='all, delete-orphan', lazy=True)

    quality_sheets = db.relationship('QualitySheet', backref=backref('well_type'), lazy=True,
                                     cascade="all, delete, delete-orphan")

    def __repr__(self):
        return self.name


class Wellbore(BaseDate):
    __human_name__ = 'Секция'

    __table_args__ = (
        db.UniqueConstraint('name', 'wellbore_type_id', 'well_id', name='unique_wellbore_type'),
    )
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(128), nullable=False)
    wellbore_type_id = db.Column(db.Integer, db.ForeignKey('wellbore_type.id'), nullable=False)
    well_id = db.Column(db.Integer, db.ForeignKey('well.id'), nullable=False)

    is_gis = db.Column(db.Boolean, default=False)
    is_gti = db.Column(db.Boolean, default=False)

    quality_sheets = db.relationship('QualitySheet', backref=backref('wellbore'), lazy=True,
                                     cascade="all, delete, delete-orphan")

    gti_row = db.relationship('GtiTableRow', backref=backref('wellbore'), uselist=False, lazy=True,
                                     cascade="all, delete, delete-orphan")


    def __repr__(self):
        return self.name


class WellboreType(BaseDate):
    __human_name__ = 'Тип секции'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)

    wellbore = db.relationship('Wellbore', uselist=False, backref=backref('wellbore_type'),
                                cascade='all, delete-orphan', lazy=True)

    quality_sheets = db.relationship('QualitySheet', backref=backref('wellbore_type'), lazy=True,
                                     cascade="all, delete, delete-orphan")

    def __repr__(self):
        return self.name


class Suite(BaseDate):
    __human_name__ = 'Свита'

    __table_args__ = (
        db.UniqueConstraint('name', 'field_id', name='unique_suite'),
    )
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(64), nullable=False)
    field_id = db.Column(db.Integer, db.ForeignKey('field.id'), nullable=False)
    layers = db.relationship('Layer', backref=backref('suite'), lazy=True,
                                     cascade="all, delete, delete-orphan")

    def __repr__(self):
        return self.name


class Layer(BaseDate):
    __human_name__ = 'Пласт'

    __table_args__ = (
        db.UniqueConstraint('name', 'suite_id', name='unique_layer'),
    )
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(64), nullable=False)
    suite_id = db.Column(db.Integer, db.ForeignKey('suite.id'), nullable=False)
    path_to_files = db.relationship('FilePath', backref=backref('layer'), lazy=True,
                                     cascade="all, delete, delete-orphan")

    def __repr__(self):
        return self.name


class CompanyEmail(BaseDate):

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('service_company.id'), nullable=False)

    def __repr__(self):
        return self.email


class CustomerEmail(BaseDate):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)

    def __repr__(self):
        return self.email


class FilePath(BaseDate):
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(256), nullable=False)
    layer_id = db.Column(db.Integer, db.ForeignKey('layer.id'), nullable=False)

    def __repr__(self):
        return self.path.split('\\')[-1]


class ServiceCompany(BaseDate):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    quality_sheets = db.relationship('QualitySheet', backref=backref('service_company'), lazy=True)
    tools = db.relationship('Tool', backref=backref('service_company'), lazy=True,
                                     cascade="all, delete, delete-orphan")
    emails = db.relationship('CompanyEmail', backref=backref('service_company'), lazy=True,
                                     cascade="all, delete, delete-orphan")


    def __repr__(self):
        return self.name


class Tool(BaseDate):
    __human_name__ = 'Прибор ГИС'
    __tablename__ = 'tool'
    tool_type = db.Column(db.String(128))
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('service_company.id'), nullable=False)

    # is_overdue = db.Column(db.Bool)

    def __repr__(self):
        return self.name
