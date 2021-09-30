from flask import Flask, request, Response
from database.db import initialize_db
from database.models import Animal

app = Flask(__name__)

# movies = [
#     {
#         "name": "The Shawshank Redemption",
#         "casts": ["Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler"],
#         "genres": ["Drama"]
#     },
#     {
#        "name": "The Godfather ",
#        "casts": ["Marlon Brando", "Al Pacino", "James Caan", "Diane Keaton"],
#        "genres": ["Crime", "Drama"]
#     }
# ]


app.config['MONGODB_SETTINGS'] = {
    'host' : 'mongodb://localhost/animal-bag'
}
initialize_db(app)


@app.route('/animals')
def get_animal():
    animals = Animal.objects().to_json()
    return Response(animals, mimetype="application/json", status=200)


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