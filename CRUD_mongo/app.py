from flask import Flask, render_template, request, redirect, url_for
import pymongo
from bson.objectid import ObjectId

app = Flask(__name__)

database_name = "test"
mongo_pass = "Imhvns.100" #test password
DB_URI = "mongodb+srv://database_learning:{}@cluster0.bpmpc.mongodb.net/{}?retryWrites=true&w=majority".format(mongo_pass, database_name)
client = pymongo.MongoClient(DB_URI)
db = client["API"]
animals_db = db["animals"]


@app.route("/")
def home():
    return render_template('index.html', members=animals_db.find())


@app.route("/animals/create")
def create():
    return render_template('create.html')


@app.route("/animals/save", methods=['POST'])
def save():
    animal = request.form['animal']
    age = request.form['age']
    gender = request.form['gender']
    color = request.form['color']

    data = {"animal": animal, "age": age, "gender": gender, "color": color}

    animals_db.insert_one(data)
    return redirect(url_for('home'))


@app.route("/animals/edit/<string:id>")
def edit(id):
    result = animals_db.find_one({"_id": ObjectId(id)})
    return render_template('edit.html', member=result)


@app.route("/animals/update", methods=['POST'])
def update():
    id = request.form['id']
    animal = request.form['animal']
    age = request.form['age']
    gender = request.form['gender']
    color = request.form['color']

    data = {"animal": animal, "age": age, "gender": gender, "color": color}

    animals_db.update_one({'_id': ObjectId(id)}, {"$set": data}, upsert=False)
    return redirect(url_for('home'))


@app.route("/animals/delete/<string:id>", methods=['GET', 'DELETE'])
def delete(id):
    if request.method == 'DELETE':
        if request.json:
            params = request.json
        else:
            params = request.form

        id = params.get('id')

    animals_db.remove({"_id": ObjectId(id)})
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
