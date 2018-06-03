# try - catch block is used as try-except block
data = {
    "name": "Saurabh"
}

try:
    print(data["age"])
except KeyError:
    print("Error finding age")

# we can chain exception to handle multiple error

try:
    print(data["age"])
except KeyError:
    print("Error finding age")
except TypeError:
    print("Handling another error")

# or just except the generic "Exception"

try:
    print(data["age"])
except Exception as error:
    print("Error finding age")
    print(error)

