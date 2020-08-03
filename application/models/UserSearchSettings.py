from application import db
from datetime import datetime
from sqlalchemy.orm import backref


class UserSearchSettings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    search_name = db.Column(db.String(256))
    folder = db.relationship('Customer')