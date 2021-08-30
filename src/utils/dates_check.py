from ..models import User
from datetime import datetime

def no_overlapping_dates(user_id, start_date, end_date):
    """
    method to check for overlapping dates for visit 
    of the user
    """
    user = User.query.get(user_id)
    if len(user.visits):
        for i in user.visits:
            if (
                datetime.fromisoformat(str(i.start_date)) < 
                datetime.fromisoformat(str(start_date)) < 
                datetime.fromisoformat(str(i.end_date))
            ) or (
                datetime.fromisoformat(str(i.start_date)) < 
                datetime.fromisoformat(str(end_date)) < 
                datetime.fromisoformat(str(i.end_date))
            ):
                return False
    return True