from application import db
from datetime import datetime
from sqlalchemy.orm import backref

from application.models.base.base_date import BaseDate


class GtiFormat(BaseDate):
    __human_name__ = 'Формат ГТИ'
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(128), nullable=False)

    parameter_id = db.Column(db.Integer, db.ForeignKey('gti_parameter.id'), nullable=False)

    def __repr__(self):
        return self.name