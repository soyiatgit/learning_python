# all blocks in python are created using a : and indentation.
# There is no usage of {} for blocks in python

# pip is the package manager for python
# to install a python package use pip install <module_name>
# details of all python packages can be obtained at pypi.python.org

number = 5;
num = 6;
if number == 5 :
    print("Yes");
else:
    print("No");

# for checking booleans and other condition, python has the same concept of
# truthy and falsy as in JS

# && and || are used as and/or

if number == 5 and num == 6:
    print("True");

# Ternary statement are written as

print("true" if number < num else "false")