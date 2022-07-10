from email.policy import default
from enum import unique

from email.policy import default
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))

    def is_active(self):
        """True, as all users are active."""
        return True