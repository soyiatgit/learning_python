# functions are similar to what they are in nay other language
# they are declared using def


def add(a, b):
    return a+b

# default args


def add(a, b=0):
    return a+b


# variable args is one of the imp and special feature of python


def var_args(name, *args):
    print(args)

# usage
# all extra args are assigned to the args parameter in the function call
# this parameter is available as args inside the function as a list


var_args('Saurabh', 1,2, True, None);


# keyword arguments


def key_word_args(name, **kwargs):
    print(name);
    print(kwargs);


# usage, just send the extra args with their name and retrieve them by name in body
# instead of index as in case of *args


key_word_args('Saurabh', age=12, hobby="code");






