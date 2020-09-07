from application import db
from sqlalchemy.orm import backref

from application.models.base.base_date import BaseDate
from .quality_sheet.quality_sheet import GtiQualitySheet
from .directory.service_company import GtiServiceCompany
from .quality_sheet.final_report import GtiFinalReport


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
    frequency = db.Column(db.Integer, default=0)
    quality = db.Column(db.Integer, db.ForeignKey('gti_table_row_quality.id'))
    authors = db.relationship('User', secondary=author_gti_row, backref='authors')

    notes = db.Column(db.String(512))

    final_report_id = db.Column(db.Integer, db.ForeignKey('gti_final_report.id'))
    final_report_path = db.Column(db.String(256))

    gti_quality_sheet = db.relationship('GtiQualitySheet',
                                        backref=backref('gti_table_row'),
                                        lazy=True,
                                        uselist=False,
                                        cascade='all, delete, delete-orphan')

    date_T3 = db.Column(db.DateTime)

    service_company_id = db.Column(db.Integer, db.ForeignKey('gti_service_company.id'))
    station_type_id = db.Column(db.Integer, db.ForeignKey('gti_station_type.id'))
    degasser_type_id = db.Column(db.Integer, db.ForeignKey('gti_degasser_type.id'))
    chromatograph_type_id = db.Column(db.Integer, db.ForeignKey('gti_chromatograph_type.id'))
    factory_num = db.Column(db.String(128))



