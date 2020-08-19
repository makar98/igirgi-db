from application import db
from sqlalchemy.orm import backref
from application.models.base.base_date import BaseDate


class GtiDegasserType(BaseDate):
    __human_name__ = 'Тип дегазатора'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, unique=True)

    gti_rows = db.relationship('GtiTableRow',
                               backref=backref('degasser_type'),
                               lazy=True,
                               cascade='all, delete, delete-orphan')
