from application import db
from datetime import datetime
from sqlalchemy.orm import backref



class Logger(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    date = db.Column(db.DateTime, default=datetime.utcnow)

    editable_tbl = db.Column(db.String(128))

    is_create = db.Column(db.Boolean, default=False)
    is_edit = db.Column(db.Boolean, default=False)
    is_delete = db.Column(db.Boolean, default=False)

    editable_fields = db.relationship('EditableField', backref=backref('logger'), lazy=True)



class EditableField(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    log_id = db.Column(db.Integer, db.ForeignKey('logger.id'))

    field_name = db.Column(db.String(128))
    before_edit = db. Column(db.String(1024))
    after_edit = db. Column(db.String(1024))

    def __repr__(self):
        if self.logger.is_edit:
            return f'Пользователь {self.logger.user.username} изменил поле {self.field_name} ' \
                   f'в таблице {self.logger.editable_tbl} c ' \
                   f'{self.before_edit} на {self.after_edit} в {self.logger.date}'

        if self.logger.is_create:
            return f'Пользователь {self.logger.user.username} создал поле {self.field_name} ' \
                   f'в таблице {self.logger.editable_tbl} со значением {self.after_edit} в {self.logger.date}'

        if self.logger.is_delete:
            return f'Пользователь {self.logger.user.username} удалил запись {self.before_edit} ' \
                   f'Из таблицы {self.logger.editable_tbl}'