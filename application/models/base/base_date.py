from application import db
from datetime import datetime
from sqlalchemy.orm import backref


class BaseDate(db.Model):
    __abstract__ = True
    create_date = db.Column(db.DateTime, default=datetime.now())
    edit_date = db.Column(db.DateTime, default=datetime.now())

