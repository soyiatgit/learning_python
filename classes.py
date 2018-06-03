# class is created using a class keyword and is almost similar to classes in other language


class Student:

    # defining class level or static variable, from the functions of class, this can be
    # accessed using self.school_name. While outside the class this can be used using
    # the class name, ex: Student.school_name
    school_name = 'DBS'

    # constructor in python are declared using the __init__ key word
    def __init__(self):
        # declaring instance variable here
        self.name = 'Saurabh'
        self.age = 25
        print("I am inside constructor")

    # a special method __str__ stringifies an object of the class. This is automatically called
    # when you print() an instance of any class. We can override this method to print what we need

    # for each function declared in a class, a first mandatory parameter is self
    # the self refers to the class instance (like this in other language)
    # all methods of class when called from the class are called using self
    # ex: self.add_student();
    # outside the class such methods are called using an instance of this class

    def add_student(self, name):
        print(name)

    def get_school_name(self):
        return self.school_name

# inheritance and polymorphism works very much the same as Java except that
# a child class is written as below
# which means ChildStudent class derives from Student class or say extends it in Java terminology

class ChildStudent(Student):

    # all methods in python are public as there are no access modifiers
    # hence we can override all the methods if needed
    # the super() inside a child class method refers to the self in parent class
    # also there is no interfaces in python
    def get_school_name(self):
        original_name = super().get_school_name()
        print(original_name + "--CS")





