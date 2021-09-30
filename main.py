from flask import Flask
from flask.signals import message_flashed
from flask_restful import Api, Resource, abort, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class AnimalModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    animal = db.Column(db.String(25), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    mass = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String(20), nullable=False)
    
    def __repr__(self):
        return f"Animal(animal = {AnimalModel.animal}, age = {AnimalModel.age}, gender={AnimalModel.gender}, mass={AnimalModel.mass}, color={AnimalModel.color})"

db.create_all()

animal_put_args = reqparse.RequestParser()
animal_put_args.add_argument("animal", type=str, help="What is the animal", required = True)
animal_put_args.add_argument("age", type=int, help="Age of the animal", required = True)
animal_put_args.add_argument("gender", type=str, help="Gender of the animal", required = True)
animal_put_args.add_argument("mass", type=int, help="Mass of the animal", required = True)
animal_put_args.add_argument("color", type=str, help="Color of the animal", required = True)

animal_update_args = reqparse.RequestParser()
animal_update_args.add_argument("animal", type=str, help="What is the animal")
animal_update_args.add_argument("age", type=int, help="Age of the animal")
animal_update_args.add_argument("gender", type=str, help="Gender of the animal")
animal_update_args.add_argument("mass", type=int, help="Mass of the animal")
animal_update_args.add_argument("color", type=str, help="Color of the animal")


resourse_fields = {
    'id': fields.String,
    'animal': fields.String,
    'age': fields.Integer,
    'gender': fields.String,
    'mass': fields.Integer,
    'color': fields.String
}

class Animals(Resource):
    @marshal_with(resourse_fields)
    def get(self, animal_id):
        result = AnimalModel.query.filter_by(id=animal_id).first()
        if not result:
            abort(404, message="Could not find animal with that id")
        return result

    @marshal_with(resourse_fields)
    def put(self, animal_id):
        args = animal_put_args.parse_args()
        result = AnimalModel.query.filter_by(id=animal_id).first()
        if result:
            abort(409, message="animal_id taken ...")
        animal = AnimalModel(
            id=animal_id,
            animal=args['animal'],
            age=args['age'],
            gender=args['gender'],
            mass=args['mass'],
            color=args['color']
            )
        db.session.add(animal)
        db.session.commit()
        return animal, 201
    
    def patch(self, animal_id):
        args = animal_update_args.parse_args()
        result = AnimalModel.query.filter_by(id=animal_id).first()
        if not result:
            abort(404, message="Animal does not exists...")
        if args['animal']:
            result.animal = args['animal']
        if args['age']:
            result.age = args['age']
        if args['gender']:
            result.gender = args['gender']
        if args['mass']:
            result.mass = args['mass']
        if args['color']:
            result.color = args['color']
        
        db.session.commit()
        return result

#    def delete(self, animal_id):
#        args = animal_update_args.parse_args()
#        result = AnimalModel.query.filter_by(id=animal_id).first()
#        if result:
#            abort(409, message="animal id not exists..."
#        return result

api.add_resource(Animals, "/animal/<int:animal_id>")

if __name__=="__main__":
    app.run(debug=True)
