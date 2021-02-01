from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#from flask_login import LoginManager
from flask_security import Security, SQLAlchemyUserDatastore
from application.forms import ExtendedLoginForm
from flask_restful import Api
from flask_marshmallow import Marshmallow
#from flask_cors import CORS

app = Flask(__name__, static_folder='static')
app.config.from_object(Config)
#CORS(app)

db = SQLAlchemy(app, engine_options={'pool_size': 10, 'max_overflow': -1})

""" Users & Roles """
from application.models.user import User, Role

migrate = Migrate(app, db)

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore,
                    login_form=ExtendedLoginForm)
"""###"""

""" API """
ma = Marshmallow(app)

from application.api.routes import initialize_routes
api = Api(app)
initialize_routes(api)
"""###"""

# Импорт моделей делать после db
# https://stackoverflow.com/questions/50308051/importerror-cannot-import-name-db
""" Admin """
from .admin import create_admin

admin = create_admin(app, db)
"""###"""

from application.routes import routes
from application.routes.gti import routes

