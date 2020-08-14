from application import db
from sqlalchemy.orm import backref
from datetime import datetime

from application.models.base.base_date import BaseDate
from application.models.gti.parameter import GtiParameter
from application.models.gti.format import GtiFormat

class Row(BaseDate):
    __abstract__ = True
    interval_beg = db.Column(db.Float())
    interval_end = db.Column(db.Float())

    date = db.Column(db.DateTime, default=datetime.now())

    counterfeit = db.Column(db.String(1024))


class GtiTechnologicalResearch(Row):
    __human_name__ = 'Технологические исследования ГТИ'

    id = db.Column(db.Integer, primary_key=True)

    quality_sheet_id = db.Column(db.Integer, db.ForeignKey('gti_quality_sheet.id'))

    parameter = db.relationship('GtiParameter',
                                uselist=False,
                                backref=backref('technological_parameter'),
                                cascade='all, delete-orphan',
                                lazy=True)

    format = db.relationship('GtiFormat',
                                uselist=False,
                                backref=backref('technological_format'),
                                cascade='all, delete-orphan',
                                lazy=True)

    #format_id = db.Column(db.Integer, db.ForeignKey('format_id'))


class GtiGasResearch(Row):
    __human_name__ = 'Газовый каротаж ГТИ'


    id = db.Column(db.Integer, primary_key=True)

    quality_sheet_id = db.Column(db.Integer, db.ForeignKey('gti_quality_sheet.id'))

    parameter = db.relationship('GtiParameter',
                                uselist=False,
                                backref=backref('gas_parameter'),
                                cascade='all, delete-orphan',
                                lazy=True)

    format = db.relationship('GtiFormat',
                                uselist=False,
                                backref=backref('gas_format'),
                                cascade='all, delete-orphan',
                                lazy=True)

class GtiGeoResearch(Row):
    __human_name__ = 'Геолого-геохимичкские исследования ГТИ'

    id = db.Column(db.Integer, primary_key=True)

    quality_sheet_id = db.Column(db.Integer, db.ForeignKey('gti_quality_sheet.id'))

    parameter = db.relationship('GtiParameter',
                                uselist=False,
                                backref=backref('geo_parameter'),
                                cascade='all, delete-orphan',
                                lazy=True)

    format = db.relationship('GtiFormat',
                                uselist=False,
                                backref=backref('geo_format'),
                                cascade='all, delete-orphan',
                                lazy=True)

