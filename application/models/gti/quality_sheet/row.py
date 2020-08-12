from application import db
from sqlalchemy.orm import backref

from application.models.base.base_date import BaseDate

class Row(BaseDate):
    __abstract__ = True
    interval_beg = db.Column(db.Float())
    interval_end = db.Column(db.Float())

    date = db.Column(db.DateTime)



