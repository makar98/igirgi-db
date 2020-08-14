from application import db
from sqlalchemy.orm import backref

from application.models.base.base_date import BaseDate


class GtiParameter(BaseDate):
    __human_name__ = 'Параметр ГТИ'
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(128), nullable=False)

    formats = db.relationship('GtiFormat', backref=backref('gti_parameter'), lazy=True,
                              cascade='all, delete, delete-orphan')

    gti_technological_research_rows = db.relationship('GtiTechnologicalResearch',
                                                      backref=backref('technological_parameter'),
                                                      cascade='all, delete-orphan',
                                                      lazy=True)

    gas_research_row_id = db.relationship('GtiGasResearch',
                                                      backref=backref('gas_parameter'),
                                                      cascade='all, delete-orphan',
                                                      lazy=True)

    geo_research_row_id = db.relationship('GtiGeoResearch',
                                                      backref=backref('geo_parameter'),
                                                      cascade='all, delete-orphan',
                                                      lazy=True)

    def __repr__(self):
        return self.name
