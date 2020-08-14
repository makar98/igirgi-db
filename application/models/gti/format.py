from application import db
from datetime import datetime
from sqlalchemy.orm import backref

from application.models.base.base_date import BaseDate


class GtiFormat(BaseDate):
    __human_name__ = 'Формат ГТИ'
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(128), nullable=False)

    parameter_id = db.Column(db.Integer, db.ForeignKey('gti_parameter.id'), nullable=False)

    technological_research_row_id = db.relationship('GtiTechnologicalResearch',
                                                      backref=backref('technological_format'),
                                                      cascade='all, delete-orphan',
                                                      lazy=True)

    gas_research_row_id = db.relationship('GtiGasResearch',
                                          backref=backref('gas_format'),
                                          cascade='all, delete-orphan',
                                          lazy=True)

    geo_research_row_id = db.relationship('GtiGeoResearch',
                                          backref=backref('geo_format'),
                                          cascade='all, delete-orphan',
                                          lazy=True)

    def __repr__(self):
        return self.name