# Create a dictionary with 5 key–value pairs and print the value of a given key.
dict1 = {"name":"Tejas", 
        "surname":"Shinde", 
        "city":"Pune", 
        "age":22, 
        (2,1):[1,2]}
print(dict1.values())

# Write a program to add a new key to a dictionary and update an existing key.
dict1.update({"gender":"Male",
             "course":"Python",
             "city":"Baramati"
            })
print(dict1)

# Write a program to check whether a key exists in a dictionary.
print(dict1.get("gender",0))
print(dict1.get("District", "Not Found"))

# Write a program to remove a key from a dictionary:
dict1.popitem()
print(dict1)
del dict1[(2,1)]
print(dict1)

# Write a program to print all keys, values, and key–value pairs from a dictionary.
for key in dict1:
    print(key)
for value in dict1.values():
    print(value)
for key, value in dict1.items():
    print(f"key : {key}, value : {value}")

# Write a program to merge two dictionaries.
dict1 = {"Student1": "A",
         "Roll_noA": 234,
         "GenderA": "Male"}
print
dict2 = {"Stident2": "B",
         "Roll_noB": 432,
         "GenderB": "Female"}
dict1.update(dict2)
print(dict1)

# Write a program to find the key that has the maximum value in a dictionary.
dict_num = {"one": 23, "two": 4, "three": 879, "four": 543, "five": 76}
max_key = None
max_value = float('-inf')
for key, value in dict_num.items():
    if value > max_value:
        max_value = value
        max_key = key
print("Key with max value:", max_key ,"and max value is :", max_value)

# Write a program to swap keys and values in a dictionary.
data = {"name":"Tejas", 
        "surname":"Shinde", 
        "city":"Pune", 
        "age":22}
swapped = {}
for key, value in data.items():
    swapped[value] = key
print(swapped)

# if Dictionry contains list in value then it will be swapped as list in key which is not possible so :
dict1 = {"name":"Tejas", 
        "surname":"Shinde", 
        "city":"Pune", 
        "age":22, 
        (2,1):[1,2]}
swapped={}
for key, value in dict1.items():
    if isinstance(value, list):
        value = tuple(value)
        swapped[value] = key
print(swapped)

# Write a program to sort a dictionary by its values.
dict1 = {"name":76, 
        "surname": 345, 
        "city":654, 
        "age":22}
sorted_dict = dict(sorted(dict1.items(), key=lambda item: item[1]))
print(sorted_dict)

def get_value(item):
    return item[1]
sorted_dict = dict(sorted(dict1.items(), key=get_value))
print(sorted_dict)

# Given a nested dictionary, print a specific inner value.
data = {"name": "Tejas",
        "surname": "Shinde",
        "address":{
            "country" : "India",
            "state" : "MH",
            "district" : "Pune"
        },
        "gender": "Male"}
print(data["address"]["state"])

# Write a program to remove duplicate values from a dictionary.
data1 = {"a" : "Mumbai",
         "b": 23,
         "c": "Pune",
         "d": "Mumbai",
         "e": 65,
         "f": 23}
data2 = {}
seen_values = set()
for key, value in data1.items():
    if value not in seen_values:
        data2[key] = value
        seen_values.add(value)
print(data2)

# Write a program using dictionary comprehension to create a dictionary of numbers and their squares.
Squares = {x : x*x for x in range(1,10)}
print(Squares)