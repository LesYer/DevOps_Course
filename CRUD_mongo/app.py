from flask import Flask, request, Response
from database.db import initialize_db
from database.models import Animal
#from api_constants import mongo_pass
app = Flask(__name__)

@app.route('/')
def index():
    return "Working! Its a magic)"

animals = [
     {
         "animal": ["Dog"],
         "age": ["10"],
         "gender": ["male"],
         "mass": ["10"],
         "color": ["white"]
     },
     {
         "animal": ["Cat"],
         "age": ["4"],
         "gender": ["male"],
         "mass": ["3"],
         "color": ["black"]
     },
     {
         "animal": ["Pig"],
         "age": ["2"],
         "gender": ["female"],
         "mass": ["100"],
         "color": ["pink"]
     },
     {
         "animal": ["Hamster"],
         "age": ["4 weeks"],
         "gender": ["male"],
         "mass": ["100 g"],
         "color": ["white"]
     },
     {
         "animal": ["Snake"],
         "age": ["1 year"],
         "gender": ["female"],
         "mass": ["2 kg"],
         "color": ["yellow"]
     }
 ]

database_name = "animals"
mongo_pass = "Imhvns.100" #test password
DB_URI = "mongodb+srv://database_learning:{}@cluster0.bpmpc.mongodb.net/{}?retryWrites=true&w=majority".format(mongo_pass, database_name)

app.config['MONGODB_HOST'] = DB_URI
initialize_db(app)


@app.route('/animals')
def get_animals():
    animals = Animal.objects().to_json()
    return Response(animals, mimetype="application/json", status=200)
#   return {"Dog": "Pesdog"}

@app.route('/animals', methods=['POST'])
def add_animal():
    body = request.get_json()
    animal = Animal(**body).save()
    id = animal.id
    return {'id': str(id)}, 200


@app.route('/animals/<id>', methods=['PUT'])
def update_animal(id):
    body = request.get_json()
    Animal.objects.get(id=id).update(**body)
    return 'update', 200

@app.route('/animals/<id>', methods=['DELETE'])
def delete_animal(id):
    Animal.objects.get(id=id).delete()
    return 'delete', 200

@app.route('/animals/<id>')
def get_animal(id):
   animals = Animal.objects.get(id=id).to_json()
   return Response(animals, mimetype="application/json", status=200)


if __name__ == '__main__':
    app.run(debug=True)