from flask import Flask, request, Response, jsonify
from flask.helpers import make_response
from database.db import initialize_db
from database.models import Animal
app = Flask(__name__)

@app.route('/')
def index():
    return "Working! Its a magic)"

database_name = "test"
mongo_pass = "Imhvns.100" #test password
DB_URI = "mongodb+srv://database_learning:{}@cluster0.bpmpc.mongodb.net/{}?retryWrites=true&w=majority".format(mongo_pass, database_name)

app.config['MONGODB_HOST'] = DB_URI
initialize_db(app)

def to_json(self):

    return {
        "animal_id": self.animal_id,
        "animal": self.animal,
        "age": self.age,
        "gender": self.gender,
        "mass": self.mass,
        "color": self.color
    } 

@app.route('/test/db_animals', methods=['POST'])
def db_animals():
    a1 = Animal(
        animal_id = 1,
        animal = "Dog",
        age = 8,
        gender = "male",
        mass = "10kg",
        color = "black"
        )
    a2 = Animal(
        animal_id = 2,
        animal = "Pig",
        age = 2,
        gender = "female",
        mass = "100kg",
        color = "pink"
        )
    a1.save()
    a2.save()
#    animals = Animal.objects().to_json()
#    return Response(animals, mimetype="application/json", status=200)
    return make_response("DB ADD!", 201)

@app.route('/test/animals', methods=['GET', 'POST'])
def CR_animals():
    if request.method == "GET":
        animals = []
        for animal in Animal.objects:
            animals.append(animal)
        return make_response(jsonify(animals), 200)
    elif request.method == "POST":
        content = request.json
        animal = Animal(
            animal_id=content['animal_id'],
            animal=content['animal'],
            age=content['age'],
            gender=content['gender'],
            mass=content['mass'], 
            color=content['color']
            )
        animal.save()
        return make_response("Created", 201)
#    body = request.get_json()
#    animal = Animal(**body).save()
#    id = animal.id


@app.route('/api/animals/<animal_id>', methods=['GET', 'PUT', 'DELETE'])
def UD_animal(animal_id):
    if request.method == "GET":
        animal_obj = Animal.object("animal_id" == animal_id).first()
        if animal_obj:
            return make_response(jsonify(animal_obj.to_json()), 200)
        else:
            return make_response("Don't panic, eror", 404)
    elif request.method == "PUT":
        content=request.json
        animal_obj = Animal.object("animal_id" == animal_id).first()
        animal_obj.update(
            animal=content['animal'],
            age=content['age'],
            gender=content['gender'],
            mass=content['mass'], 
            color=content['color']
        )
        return make_response("Update", 204)
    elif request.method == "DELETE":
        animal_obj = Animal.object("animal_id" == animal_id).first()
        animal_obj.delte()
        return make_response("Delete",204)


if __name__ == '__main__':
    app.run(debug=True)