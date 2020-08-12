from application import db
from datetime import datetime

from application.models.base.base_date import BaseDate
from .row import Row


class GtiTechnologicalResearch(Row):
    __human_name__ = 'Технологические исследования ГТИ'
    id = db.Column(db.Integer, primary_key=True)

    date = db.Column(db.DateTime, default=datetime.utcnow)
    parameter = db.Column(db.String(128))
    format = db.Column(db.String(128))
    falsification = db.Column(db.String(128))


class GtiGasResearch(Row):
    __human_name__ = 'Газовый каротаж ГТИ'
    id = db.Column(db.Integer, primary_key=True)

    date = db.Column(db.DateTime, default=datetime.utcnow)
    parameter = db.Column(db.String(128))
    format = db.Column(db.String(128))
    falsification = db.Column(db.String(128))


class GtiGeoResearch(Row):
    __human_name__ = 'Геолого-геохимичкские исследования ГТИ'

    id = db.Column(db.Integer, primary_key=True)

    date = db.Column(db.DateTime, default=datetime.utcnow)
    parameter = db.Column(db.String(128))
    format = db.Column(db.String(128))
    falsification = db.Column(db.String(128))