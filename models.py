# models.py
import flask_sqlalchemy
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from Integration import db

class username(db.Model):
    __tablename__ = 'username'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(400))
    child = db.relationship("character", backref="userid")
    

class character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('username.id'))
    characterName = db.Column(db.String(400))
    str = db.Column(db.Integer)
    dex = db.Column(db.Integer)
    con = db.Column(db.Integer)
    int = db.Column(db.Integer)
    cha = db.Column(db.Integer)
    luck = db.Column(db.Integer)
    max_health = db.Column(db.Integer)
    health = db.Column(db.Integer)
    max_mana = db.Column(db.Integer)
    mana = db.Column(db.Integer)
    money = db.Column(db.Integer)
    checkpoint = db.Column(db.String(400))
    gender = db.Column(db.String(400))
    characterClass = db.Column(db.String(400))
    
    child = db.relationship("inventory", backref="characterid")
    
class inventory(db.Model):
    __tablename__ = 'inventory'
    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    items = db.Column(db.String(400))
    