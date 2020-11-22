"""
    File which handles PSQL interactions with python
"""
import flask_sqlalchemy
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from Integration import db


class username(db.Model):
    """ Stores username from login """
    __tablename__ = 'username'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(400))
    child = db.relationship("character", backref="userid")

class character(db.Model):
    """ Stores character info """
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("username.id"))
    character_name = db.Column(db.String(400))
    strength = db.Column(db.Integer)
    dex = db.Column(db.Integer)
    con = db.Column(db.Integer)
    intel = db.Column(db.Integer)
    cha = db.Column(db.Integer)
    luck = db.Column(db.Integer)
    max_health = db.Column(db.Integer)
    health = db.Column(db.Integer)
    max_mana = db.Column(db.Integer)
    mana = db.Column(db.Integer)
    money = db.Column(db.Integer)
    checkpoint = db.Column(db.String(400))
    gender = db.Column(db.String(400))
    character_class = db.Column(db.String(400))
    child = db.relationship("inventory", backref="characterid")

class inventory(db.Model):
    """ Stores character inventory """
    __tablename__ = 'inventory'
    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey("character.id"))
    items = db.Column(db.String(400))

class inventory_asc(db.Model):
    """ Stores character inventory """
    __tablename__ = 'inventory_asc'
    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey("character.id"))
    items = db.Column(db.String(400))

class inventory_dsc(db.Model):
    """ Stores character inventory """
    __tablename__ = 'inventory_dsc'
    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey("character.id"))
    items = db.Column(db.String(400))