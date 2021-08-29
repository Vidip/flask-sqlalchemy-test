from flask import jsonify, request, Response
from .models import User, db

def user():
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

def add_to_database(object):
    db.session.add(object)
    db.session.commit()