from flask import jsonify, request, Response
from .models import User, db, Visit
from sqlalchemy.sql.expression import and_
from .utils import dates_check

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
    if user_id and dates_check.no_overlapping_dates(user_id, start_date, end_date):
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
            "user_id": user_id
        })
    else:
        return {
            "Error Message": "Dates overlap with existing visit's dates",
        }, 402

def get_single_visit(id):
    visiting = get_visit_data(id)
    if visiting and type(visiting) != dict:
        visiting = visiting.__dict__
    if visiting:
        resp = {
            "id": visiting.get('id'), 
            "start_date": visiting.get('start_date'), 
            "end_date": visiting.get('end_date'), 
            "instructions": visiting.get('instructions', '')
        }
        return jsonify(resp)
    else:
        resp = {
            "message": "No results found"
        }
        return resp, 404

def get_visits(page_id, user_id = None):
    filters = {}
    if user_id: filters['user_id'] = user_id
    try:
        visits = Visit.query.with_entities(
            Visit.user_id, 
            Visit.start_date, 
            Visit.end_date
        ).filter_by(**filters).order_by(Visit.start_date.asc()).paginate(page=page_id, per_page=3, error_out=True)
        return jsonify({
            "total": visits.total, 
            "current_page": visits.page,
            "per_page": visits.per_page,
            "next_page": visits.next_num if visits.has_next else -1,
            "prev_page": visits.prev_num if visits.has_prev else -1,
            "data": [{"username": User.query.get(u.user_id).username, "start_date": u.start_date, "end_date": u.end_date} for u in visits.items],
        })
    except Exception as e:
        resp = jsonify({"error": str(e)})
        resp.status_code = 500
        return resp

def get_visit_data(id):
    try:
        return Visit.query.get(id)
    except Exception as e:
        raise Exception("Issue with Data Fetching")

def add_to_database(object):
    """
    generic function to add to the database session
    db close call is handled automaitcally by the SQLAlchemy session
    """
    db.session.add(object)
    db.session.commit()

