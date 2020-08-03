import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    FLASK_APP = os.environ.get('FLASK_APP') or 'main.py'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql+pymysql://a_makeev:Cgfhnfr18011998@localhost:3306/igirgi_empty'
        #'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_HASH = 'bcrypt'
    SECURITY_USER_IDENTITY_ATTRIBUTES = ('username','email')

