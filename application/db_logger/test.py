from application.db_logger.db_logger import DBLog
from application.models.models import Well
from application.models.logger import Logger, EditableField

from datetime import datetime

log = DBLog(user_id=1, date=datetime.now(), editable_tbl=Well,
            editable_fields=[
                {'field': 'name',
                 'before_edit': '12',
                 'after_edit': 'qwerty'},
                {'field': 'field_id',
                 'before_edit': '273',
                 'after_edit': '9874'},
                {'field': 'qwe',
                 'before_edit': '273',
                 'after_edit': '9874'}
            ]
            )
#log.edit()

from application import db

l = Logger.query.all()[-1]
#print(Logger.query.all())
for i in l.editable_fields:
    print(i)
#print(EditableField.query.all())