from application import db
from sqlalchemy.orm import backref
from werkzeug.security import check_password_hash
from flask_security import UserMixin, RoleMixin
from .base.base_date import BaseDate
from .logger import Logger

roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class Role(BaseDate, RoleMixin):
    __human_name__ = 'Роль пользователя'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class User(BaseDate, UserMixin):
    __human_name__ = 'Пользователь'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

    change_log = db.relationship('Logger', backref=backref('user'), lazy=True)

    def __repr__(self):
        return self.username

    #def set_password(self, password):
        #self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
