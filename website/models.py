from sqlalchemy import Numeric
from sqlalchemy.orm import relationship

from . import db
from flask_login import UserMixin


class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(60))
    service_detail = db.Column(db.String(5005))
    service_price = db.Column(Numeric(8,2))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = relationship("User", back_populates="services")


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    first_name = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    services = db.relationship('Service')
