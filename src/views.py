from flask import jsonify, request, Response
from .models import User, db, Visit
from datetime import datetime

def user():
    """method to create and fetch users"""
    if request.method == 'POST':
        username = request.json.get("username")
        user = User(username=username)
        try:
            add_to_database(user)
        except Exception as e:
            resp = jsonify({"error": str(e)})
            resp.status_code = 500
            return resp
        else:
            return jsonify({
                "id": user.id,
                "username": user.username
            })
    elif request.method == 'GET':
        users = User.query.filter().all()
        resp = [{"id": u.id, "username": u.username} for u in users]
        return jsonify(resp)

def create_visit():
    """
    method to create new visit and check for overlapping dates
    """
    start_date = request.json.get("start_date")
    end_date = request.json.get("end_date")
    user_id = request.json.get("user_id")
    instructions = request.json.get("instructions")
    user_id = int(user_id) if user_id else None
    if user_id and no_overlapping_dates(user_id, start_date, end_date):
        visit = Visit(
            start_date=start_date, 
            end_date=end_date, 
            user_id= user_id, 
            instructions=instructions
        )
        try:
            add_to_database(visit)
        except Exception as e:
            resp = jsonify({"error": str(e)})
            resp.status_code = 500
            return resp
        return jsonify({
            "id": 1,
            "username": "aa"
        })
    else:
        return {
            "Error Message": "Dates overlap with existing visit's dates",
        }, 402

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

def add_to_database(object):
    """
    generic function to add to the database session
    db close call is handled automaitcally by the SQLAlchemy session
    """
    db.session.add(object)
    db.session.commit()