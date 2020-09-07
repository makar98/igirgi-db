from application import db
from sqlalchemy.orm import backref
from application.models.base.base_date import BaseDate


class GtiFinalReport(BaseDate):
    __human_name__ = 'Финальный отчет ГТИ'
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(128))
    gti_rows = db.relationship('GtiTableRow',
                               backref=backref('gti_final_report'),
                               lazy=True,
                               cascade='all, delete, delete-orphan')

