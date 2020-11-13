# models.py
import flask_sqlalchemy
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from Integration import DB

class username(DB.Model):
    __tablename__ = 'username'
    id = DB.Column(DB.Integer, primary_key=True)
    email = DB.Column(DB.String(400))
    child = DB.relationship("character", backref="userid")
    

class character(DB.Model):
    __tablename__ = 'character'
    id = DB.Column(DB.Integer, primary_key=True)
    user_id = DB.Column(DB.Integer, DB.ForeignKey('username.id'))
    
    characterName = DB.Column(DB.String(400))
    strength = DB.Column(DB.Integer)
    dex = DB.Column(DB.Integer)
    con = DB.Column(DB.Integer)
    intel = DB.Column(DB.Integer)
    cha = DB.Column(DB.Integer)
    luck = DB.Column(DB.Integer)
    max_health = DB.Column(DB.Integer)
    health = DB.Column(DB.Integer)
    max_mana = DB.Column(DB.Integer)
    mana = DB.Column(DB.Integer)
    money = DB.Column(DB.Integer)
    
    child = DB.relationship("inventory", backref="characterid")
    
    
class inventory(DB.Model):
    __tablename__ = 'inventory'
    id = DB.Column(DB.Integer, primary_key=True)
    character_id = DB.Column(DB.Integer, DB.ForeignKey('character.id'))
    items = DB.Column(DB.String(400))
    