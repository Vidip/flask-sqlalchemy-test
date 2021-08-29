"""Application routes."""
from flask import current_app as app
from datetime import datetime
from . import views

app.add_url_rule('/users', view_func=views.user, methods=["GET", "POST"])