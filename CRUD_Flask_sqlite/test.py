import requests

BASE="http://127.0.0.1:5000/"

data =[
    {"animal": "Dog", "age": 7, "gender": "male", "mass": 10, "color": "white"},
    {"animal": "Cat", "age": 4, "gender": "female", "mass": 5, "color": "black"},
    {"animal": "Pig", "age": 2, "gender": "female", "mass": 120, "color": "pink"}
]

for i in range(len(data)):
    response = requests.put(BASE + "animal/" + str(i+1), data[i])
    print(response.json())


input()
response = requests.get(BASE + "animal/2")
print(response.json())
input()
response = requests.patch(BASE + "animal/2", {"mass":8})
#print(response.json())
input()
response = requests.get(BASE + "animal/2")
print(response.json())
