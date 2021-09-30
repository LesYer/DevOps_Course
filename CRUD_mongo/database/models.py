from .db import db 

class Animal(db.Document):
    animal = db.StringField(required=True, unique=True)
    age = db.ListField(db.StringField(), required=True)
    gender = db.ListField(db.StringField(), required=True)
    mass = db.ListField(db.StringField(), required=True)
    color = db.ListField(db.StringField(), required=True)