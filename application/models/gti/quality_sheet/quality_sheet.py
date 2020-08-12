from application import db
from sqlalchemy.orm import backref
from application.models.base.base_date import BaseDate


class GtiQualitySheet(BaseDate):
    __human_name__ = 'Чек-лист ГТИ'
    id = db.Column(db.Integer, primary_key=True)

    gti_table_row_id = db.Column(db.Integer, db.ForeignKey('gti_table_row.id'), nullable=False)







