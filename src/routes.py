"""Application routes."""
from flask import current_app as app
from datetime import datetime
from . import views

"""routes for the project - can be optimized by gaving Lazy View for each View function"""
app.add_url_rule('/users', view_func=views.user, methods=["GET", "POST"])
app.add_url_rule('/visit', view_func=views.create_visit, methods=["POST"])
app.add_url_rule('/visit/<int:id>', view_func=views.get_single_visit, methods=["GET"])
app.add_url_rule('/visits/page/<int:page_id>', view_func=views.get_visits, methods=["GET"])
app.add_url_rule('/visits/page/<int:page_id>/<int:user_id>', view_func=views.get_visits, methods=["GET"])
