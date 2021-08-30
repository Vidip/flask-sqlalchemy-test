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

class Visit(db.Model, Base):
    __tablename__ = "visit"
    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.DateTime, nullable=False, default=TODAY_DATE_TIME)
    end_date = db.Column(db.DateTime, nullable=False, default=TODAY_DATE_TIME)
    instructions = db.Column(db.Text, index=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)

    def __repr__(self):
        return "<Visit {}>".format(self.id)

    @validates('start_date')
    def validate_start_date(self, key, start_date):
        """validator for start date - serializer"""
        formated_date = datetime.datetime.fromisoformat(str(start_date))
        if formated_date >= datetime.datetime.utcnow():
            return formated_date
        else:
            raise ValueError("Date is less than today's date and time")

    @validates('end_date')
    def validate_end_date(self, key, end_date):
        """validator for end date - serializer"""
        formated_date = datetime.datetime.fromisoformat(str(end_date))
        if formated_date >= datetime.datetime.utcnow():
            return formated_date
        else:
            raise ValueError("Date is less than today's date and time")