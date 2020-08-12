from datetime import datetime
from application.models.logger import Logger, EditableField
from application import db

from typing import List
from .schemas import EditableFields

class DBLog(object):
    def __init__(self, date: datetime, user_id: int, editable_tbl: object,
                 editable_fields: List[EditableFields],
                 is_create: bool = False, is_edit: bool = False, is_delete: bool = False,
                 ):
        self.date = date
        self.user_id = user_id
        self.editable_tbl = editable_tbl
        self.editable_fields = editable_fields

        self.is_create = is_create
        self.is_edit = is_edit
        self.is_delete = is_delete

    def save(self):
        log = Logger(user_id=self.user_id, edit_date=self.date,
                     editable_tbl=self.editable_tbl.__human_name__, is_create=self.is_create, is_edit=self.is_edit,
                     is_delete=self.is_delete)

        db.session.add(log)
        db.session.flush()

        for field in self.editable_fields:
            edit_field = EditableField(log_id=log.id, field_name=field['field'], before_edit=field['before_edit'],
                                       after_edit=field['after_edit'])
            db.session.add(edit_field)

        db.session.commit()

