from application import db
from sqlalchemy.orm import backref

from application.models.base.base_date import BaseDate


class GtiParameter(BaseDate):
    __human_name__ = 'Параметр ГТИ'
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(128), nullable=False)

    formats = db.relationship('GtiFormat', backref=backref('gti_parameter'), lazy=True,
                              cascade='all, delete, delete-orphan')

    def __repr__(self):
        return self.name
