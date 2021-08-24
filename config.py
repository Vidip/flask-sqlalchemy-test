"""Flask configuration variables."""


class Config:
    """Set Flask configuration"""

    # Database
    # SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
