# its essentially same as a JSON object, which is used to store data in python

data = {
    "name": 'Saurabh',
    "age": 12
}

# retrieval

data["age"] == 12;

# if the key is not found, a KeyError is thrown

data.keys() == ["name","age"];
data.values() == ["Saurabh",12];

del data["age"]; # deletes the age key


