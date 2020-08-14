from application import db
from sqlalchemy.orm import backref

from application.models.base.base_date import BaseDate


class GtiParameter(BaseDate):
    __human_name__ = 'Параметр ГТИ'
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(128), nullable=False)

    formats = db.relationship('GtiFormat', backref=backref('gti_parameter'), lazy=True,
                              cascade='all, delete, delete-orphan')

    technological_research_row_id = db.Column(db.Integer,
                                              db.ForeignKey('gti_technological_research.id'),
                                              nullable=False)

    gas_research_row_id = db.Column(db.Integer,
                                              db.ForeignKey('gti_gas_research.id'),
                                              nullable=False)

    geo_research_row_id = db.Column(db.Integer,
                                              db.ForeignKey('gti_geo_research.id'),
                                              nullable=False)

    def __repr__(self):
        return self.name
