"""Application routes."""
from flask import current_app as app
from flask import jsonify, request

from .models import User, db


@app.route("/users", methods=["POST"])
def create_user():
    username = request.json.get("username")
    user = User(username=username)
    try:
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        resp = jsonify({"error": str(e)})
        resp.status_code = 500
        return resp
    else:
        return jsonify({
            "id": user.id,
            "username": user.username
        })


@app.route("/users", methods=["GET"])
def get_users():
    users = User.query.filter().all()
    resp = [{"id": u.id, "username": u.username} for u in users]
    return jsonify(resp)

