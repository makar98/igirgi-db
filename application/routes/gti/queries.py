from application.models.user import User
from application.models.gti.table_row import GtiTableRow
from application.models.models import Layer
from application.models.models import Wellbore

from sqlalchemy import or_, and_, asc, desc
from flask_security import login_required, current_user
from datetime import datetime

from typing import List


def gti_row_query(quality_id: List[int]):

    print(quality_id)
    """
    for key, value in kwargs.items():
        gti_rows = GtiTableRow.query.filter(and_(GtiTableRow.edit_date >= date_interval,
                                                 or_(GtiTableRow.authors.any(User.id.in_(users_id))))
                                            ).all()
    
    , date_T3: datetime, wellbore_status_id: List[int], final_report_id: List[int],
                  service_company_id: List[int], station_type_id: List[int], degasser_type_id:List[int],
                  chromatograph_type_id: List[int], factory_num: int, layers_id: List[int]):
    """