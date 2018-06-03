# we can import the files in python using various ways

# importing the entire file, this way you need to specify what you are using
# ex classes.Student

import classes

student = classes.Student()
print(student.get_school_name())

# also we can import specific item from a file

from classes import ChildStudent

child_student = ChildStudent()
print(child_student.get_school_name())

# or we can import everything from a file using *

from classes import *

child_student = ChildStudent()
print(child_student.get_school_name())


