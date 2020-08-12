from flask_restful import Resource
from application.models.logger import Logger
from .logger import logger_schema, loggers_schema
from flask_restful import reqparse
from datetime import datetime, timedelta

from sqlalchemy import or_, and_, asc, desc


from flask_security import login_required, current_user

from application.db_logger import methods

class LoggerApi(Resource):
    @login_required
    def get(self, log_id):
        #logger = Logger.query.filter_by(id=log_id).first_or_404()
        logger = Logger.query.filter_by(id=log_id).first()
        print(logger)
        return logger_schema.jsonify(logger)


class LoggersApi(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('users')
        parser.add_argument('date_interval')
        parser.add_argument('sort')
        args = parser.parse_args()
        users_id = args['users'].split(',')

        if args['date_interval'] == 'last_hour':
            date_interval = datetime.now()  - timedelta(hours=1)

        if args['date_interval'] == 'last_day':
            date_interval = datetime.now()  - timedelta(days=1)

        if args['date_interval'] == 'last_week':
            date_interval = datetime.now()  - timedelta(weeks=1)

        if args['date_interval'] == 'last_month':
            date_interval = datetime.now()  - timedelta(days=30)

        if args['date_interval'] == 'all_time':
            date_interval = datetime(1990, 3, 5)

        if args['sort'] == 'asc':
            loggers = Logger.query.filter(and_(Logger.edit_date >= date_interval,
                                               or_(Logger.user_id==id for id in users_id))
                                          ).order_by(asc(Logger.edit_date)).all()
            return loggers_schema.jsonify(loggers)

        if args['sort'] == 'desc':
            loggers = Logger.query.filter(and_(Logger.edit_date >= date_interval,
                                               or_(Logger.user_id==id for id in users_id))
                                          ).order_by(desc(Logger.edit_date)).all()
            return loggers_schema.jsonify(loggers)

