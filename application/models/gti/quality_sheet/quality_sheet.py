from application import db
from sqlalchemy.orm import backref
from application.models.base.base_date import BaseDate

from .row import GtiTechnologicalResearch, GtiGasResearch, GtiGeoResearch


class GtiQualitySheet(BaseDate):
    __human_name__ = 'Чек-лист ГТИ'
    id = db.Column(db.Integer, primary_key=True)

    gti_table_row_id = db.Column(db.Integer, db.ForeignKey('gti_table_row.id'), nullable=False)

    rows_technological = db.relationship('GtiTechnologicalResearch',
                                        backref=backref('quality_sheet'),
                                        lazy=True,
                                        cascade='all, delete, delete-orphan')
    rows_gas = db.relationship('GtiGasResearch',
                                        backref=backref('quality_sheet'),
                                        lazy=True,
                                        cascade='all, delete, delete-orphan')
    rows_geo = db.relationship('GtiGeoResearch',
                                        backref=backref('quality_sheet'),
                                        lazy=True,
                                        cascade='all, delete, delete-orphan')







