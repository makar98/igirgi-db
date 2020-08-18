import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = ("mysql+pymysql://"+ os.environ['DB_USER'] + ":"
                                         + os.environ['DB_PASSWORD']+ "@"
                                         + os.environ['DB_HOST']
                                         + ":3306/igirgi_empty")

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_HASH = 'bcrypt'
    SECURITY_USER_IDENTITY_ATTRIBUTES = ('username','email')

