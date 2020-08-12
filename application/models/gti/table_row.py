from application import db
from sqlalchemy.orm import backref

from application.models.base.base_date import BaseDate
from .quality_sheet.quality_sheet import GtiQualitySheet


author_gti_row = db.Table('author_gti',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('table_row_id', db.Integer, db.ForeignKey('gti_table_row.id'))
)


class GtiTableRow(BaseDate):
    __human_name__ = 'Строка таблицы ГТИ'
    id = db.Column(db.Integer, primary_key=True)

    wellbore_id = db.Column(db.Integer, db.ForeignKey('wellbore.id'), nullable=False)

    layer = db.Column(db.String(128)) #  Сделать связь к модели Layer
    company = db.Column(db.String(128)) #  Сделать связь к модели GtiServiceCompany
    efficiency = db.Column(db.String(128))
    mud_gas_quality =db.Column(db.String(128))
    frequency = db.Column(db.Integer, default=0)
    bottom_hole_plus_igti = db.Column(db.String(128))
    bottom_hole = db.Column(db.String(128))

    authors = db.relationship('User', secondary=author_gti_row, backref='authors')

    degasser = db.Column(db.String(128))
    notes = db.Column(db.String(512))

    gti_quality_sheet = db.relationship('GtiQualitySheet', backref=backref('gti_table_row'),
                                        uselist=False, lazy=True,
                                        cascade="all, delete, delete-orphan")
