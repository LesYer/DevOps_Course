from enum import unique
from .db import db 

class Animal(db.Document):
    animal_id = db.IntField(required=True, unique=True)
    animal = db.StringField(required=True)
    age = db.IntField()
    gender = db.StringField()
    mass = db.StringField()
    color = db.StringField()