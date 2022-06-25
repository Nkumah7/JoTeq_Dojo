# Dictionary 
# Uses key: value pairs

uk_trips = {
    "London": ["Chelsea stadium", "London Bridge"],
    "Manchester": "Old Trafford",
    "Liverpool": {"restaurants": ["The Alchemist"],
                  "Chilling": "Liverpool cinema"
                  }
}

restuarant_tables = {
    1: 4,
    2: 3,
    3: {"Okenna family": 2,
        "Joseph family": 4}
}
# print(uk_trips)
# print(restuarant_tables)
empty = {}

# Add a key
uk_trips['Leicester'] = "Amusement Park"
# print(uk_trips)

# Add multiple keys
restuarant_tables.update({
    4: 7,
    5: 12
})

# print(restuarant_tables)

# restuarant_tables = {
#     6: 9,
#     7: 10
# }
# print(restuarant_tables)
# uk_trips['London'] = "London Ocean"
# print(uk_trips)

# Dict Comprehensions
python_students_names = ["Okenna", "Joseph", "Ronaldo", "Messi"]
number_of_balon_dor = [1, 1, 5, 7]
# data = zip(python_students_names, number_of_balon_dor)
# dict_comprehension = {operation | for temporary variable in | collection}
students = {key: value for key, value in zip(python_students_names, number_of_balon_dor)}
# print(students)

# Get a key
messi_balon_dor = students["Messi"]
ronaldo_balon_dor = students["Ronaldo"]
# print(students["Joseph"])
# print(f"Messi has {messi_balon_dor} Balon D'ors")
# print(f"Ronaldo has {ronaldo_balon_dor} Balon D'ors")

# Try/Except
# try:
#     print(students["Josef"])
# except KeyError:
#     print("This key doesn't exist. Please try another key")

# get method
# joseph_balon_dor = students.get("Joseph")
# okenna_balon_dor = students.get("Okenna")
# messi = students.get("Messi", "This key does not exist")
# print(okenna_balon_dor)
# print(messi)
# print(joseph_balon_dor)

# Delete a Key
# print(uk_trips)
# removed_key = uk_trips.pop("London")
# print(removed_key)
# removed_manchester_key = print(uk_trips.pop("Manchester", "You didn't visit the city"))
# print(removed_manchester_key)
# print(uk_trips)

# Get dictionary keys

# student_names = students.keys()
# print(list(student_names))
# for name in student_names:
#     print(name)

for name in students.keys():
    print(name)
    
# Get Values
for balon_dor in students.values():
    print(balon_dor)
    
for key, value in students.items():
    print(f"{key} has {value} Balon D'ors")