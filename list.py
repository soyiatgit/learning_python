# What is array in JS is list in Python and it too has zero based index
# No types for list, you can insert whatever in a list

names = [];
names = ['Saurabh', 'Harshit'];
print(names[0]);

# indexing from the last is done using -ve index
print(names[-1]);

names.append('Navanshu');

# checking for element in python

'Saurabh' in names == True;

# length of list

print(len(names));

# deleting an element (splicing)

del(names[2]);

# slicing

print(names[1:])  # removes first element in this print not in original list
