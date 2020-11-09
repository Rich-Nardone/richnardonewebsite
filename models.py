# models.py
import flask_sqlalchemy
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from Integration import DataBase

class username(DataBase.Model):
    __tablename__ = 'username'
    id = DataBase.Column(DataBase.Integer, primary_key=True)
    email = DataBase.Column(DataBase.String(400))
    child = DataBase.relationship("character", backref="userid")
    

class character(DataBase.Model):
    __tablename__ = 'character'
    id = DataBase.Column(DataBase.Integer, primary_key=True)
    user_id = DataBase.Column(DataBase.Integer, DataBase.ForeignKey('username.id'))
    characterName = DataBase.Column(DataBase.String(400))
    child = DataBase.relationship("inventory", backref="characterid")
    
    
class inventory(DataBase.Model):
    __tablename__ = 'inventory'
    id = DataBase.Column(DataBase.Integer, primary_key=True)
    character_id = DataBase.Column(DataBase.Integer, DataBase.ForeignKey('character.id'))
    items = DataBase.Column(DataBase.String(400))