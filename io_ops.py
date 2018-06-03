# python has simple command for i/o operation

file = open("fileName.txt", "a")

# here "a" means append mode, which means if the file is not present create it

# writing to the file
file.write("Write something" + "\n")

# reading from file

try:
    file = open("fileName.txt", "r")
    for line in file.readline():
        print(line)
except FileNotFoundError as error:
    print(error)

# means open file in read mode
