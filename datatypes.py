# use print() to print something
# use input("Enter something") to let user enter something

# no data type declaration required, just make the variable and assign the data
# int declaration
number = 1

# string declaration
name = "Saurabh"
lastName = 'Tiwari'
fullName = """Saurabh Tiwari"""
"""Three quote strings can also be used as comments, 
when you need multi line comments, like this one here. 
Such a string should not be assigned to any variable"""

# string can be formatted using below two ways
formattedString = "The name is {0} and the last name is {1}".format(name, lastName)
formattedString2 = f"The name is {name} and the last name is {lastName}"
print(formattedString)
print(formattedString2)

# boolean declaration
false = False
int(false) == 0
true = True
int(true) == 1
none = None  # equivalent ot null in JS

