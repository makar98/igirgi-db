from application import db
from application.db_logger.db_logger import DBLog

from datetime import datetime


def create(editable_tbl: object, obj: object, args: dict, user: object):
    # list of editable model fields. struct at application.db_logger.db_logger EditableFields
    editable_fields = []

    for key, value in args.items():
        if value is not None:
            editable_fields.append({'field': key,
                                    'before_edit': None,
                                    'after_edit': value}
                                   )
            setattr(obj, key, value)

    db.session.commit()
    log = DBLog(user_id=user.id, date=datetime.now(), editable_tbl=editable_tbl,
                editable_fields=editable_fields, is_create=True)
    log.save()


def edit(editable_tbl: object, obj: object, args: dict, user: object):
    # list of editable model fields. struct at application.db_logger.db_logger EditableFields
    editable_fields = []

    for key, value in args.items():
        if value is not None and getattr(obj, key)!= value:
            editable_fields.append({'field': key,
                                    'before_edit': getattr(obj, key),
                                    'after_edit': value}
                                   )
            setattr(obj, key, value)

    db.session.commit()
    log = DBLog(user_id=user.id, date=datetime.now(), editable_tbl=editable_tbl,
                editable_fields=editable_fields, is_edit=True)
    log.save()


def delete(editable_tbl: object, obj: object, args: dict, user: object):
    # list of editable model fields. struct at application.db_logger.db_logger EditableFields
    editable_fields = []

    for key, value in args.items():
        if value is not None:
            editable_fields.append({'field': key,
                                    'before_edit': getattr(obj, key),
                                    'after_edit': None}
                                   )
    db.session.delete(obj)

    db.session.commit()
    log = DBLog(user_id=user.id, date=datetime.now(), editable_tbl=editable_tbl,
                editable_fields=editable_fields, is_delete=True)
    log.save()
