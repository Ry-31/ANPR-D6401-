persons = [
    {"id": "P001", "name": "Amit", "age": 25, "gender": "Male"},
    {"id": "P002", "name": "Priya", "age": 22, "gender": "Female"},
    {"id": "P003", "name": "Rahul", "age": 28, "gender": "Male"},
    {"id": "P004", "name": "Sneha", "age": 24, "gender": "Female"},
    {"id": "P005", "name": "Vikas", "age": 30, "gender": "Male"},
    {"id": "P006", "name": "Neha", "age": 27, "gender": "Female"}
]

for p in persons:
    if p["gender"] == "Male":
        p["name"] = "Mr " + p["name"]
    else:
        p["name"] = "Miss " + p["name"]

print(persons)