"""Data models."""
from . import db
import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, validates
Base = declarative_base()

TODAY_DATE_TIME = datetime.datetime.utcnow()

class User(db.Model, Base):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, index=False, unique=True, nullable=False)
    visits = db.relationship('Visit', backref='visit', lazy=True, primaryjoin="User.id == Visit.user_id")

    def __repr__(self):
        return "<User {}>".format(self.username)