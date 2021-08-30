"""Flask configuration variables."""
import os

class Config:
    """Set Flask configuration"""
    # Database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
