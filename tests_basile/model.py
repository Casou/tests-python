from enum import Enum

from sqlalchemy import Column, Integer, String, DateTime
from tests_basile import db


class Parameter(db.Model):
    __tablename__ = 'parameter'
    id = Column(Integer, primary_key=True)
    key = Column('key', String(50))
    description = Column('description', String(255))
    value = Column('value', String(255))


class ParameterEnum(Enum):
    INIT_TIMER_SECONDS = ("INIT_TIME", "Temps initial (en secondes) du timer au lancement", "3600")

    def __init__(self, key, description, default_value):
        self.key = key
        self.description = description
        self.default_value = default_value


class Token(db.Model):
    __tablename__ = 'security_token'
    id = Column('token', String, primary_key=True)
    room_name = Column('room_name', String)
    expiration_date = Column('expiration_date', DateTime)


class Riddle(db.Model):
    __tablename__ = 'riddle'
    id = Column(Integer, primary_key=True)
    name = Column('name', String)
    riddle_id = Column('riddle_id', String)
    riddle_password = Column('riddle_password', String)


class People(db.Model):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column('name', String)
    surname = Column('surname', String)
    sex = Column('sex', Integer)
    birth_date = Column('birth_date', DateTime)
    arrival_date = Column('arrival_date', DateTime)
    email = Column('email', String)
    phone = Column('phone', String)
    city = Column('city', String)
    picture_index = Column('picture_index', String)
    work_place = Column('work_place', String)
    job = Column('job', String)
    interests = db.relationship('PeopleInterest', backref='people', lazy=True)


class PeopleInterest(db.Model):
    __tablename__ = 'people_interest'
    id = Column(Integer, primary_key=True)
    name = db.Column('name', db.String(120), nullable=False)
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'), nullable=False)
