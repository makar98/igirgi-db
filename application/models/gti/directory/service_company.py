from application import db
from datetime import datetime
from sqlalchemy.orm import backref
from application.models.base.base_date import BaseDate


class GtiServiceCompany(BaseDate):
    __human_name__ = 'Подрядчик по ГТИ'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, unique=True)

    gti_rows = db.relationship('GtiTableRow',
                               backref=backref('service_company'),
                               lazy=True,
                               cascade='all, delete, delete-orphan')
