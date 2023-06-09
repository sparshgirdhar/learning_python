import math

# variable - used to store data

my_age = 27
my_age += 26
print(str(my_age))  # type casting
print(type(my_age))

# strings

name = "Sparsh"
my_age = 27

print("My name is " + name + " and my age is " + str(my_age))

print(name[3])

# study different string functions
# some are given below:

print(len(name))
print(name.find("r"))
print(name.index("S"))
name.capitalize()
name.upper()
name.lower()
name.isdigit()
name.isalpha()
name.count("S")
print(name.replace("S", "s"))

# numbers

print(4 * 5 + 3)
print(10 % 3)

age = 27
print(age)

# input

your_name = input("Enter your name: ")
your_age = input("Enter your age: ")

print("Your name is " + your_name + " and your age is " + your_age)

# study different math functions
# some are given below:

pi = 3.14

round(pi)
math.ceil(pi)
math.floor(pi)
math.sqrt(pi)
math.pow(pi, 2)
max(age, my_age)
min(age, my_age)

# string slicing
# indexing[] or using slice() function
#  [start:stop:step]


my_string = "Yamuna Nagar"

first_part = my_string[:6]
last_part = my_string[7:]
funky_name = my_string[::2]
reversed_string = my_string[::-1]

website1 = "https://google.com"
website2 = "https://wikipedia.com"

slice_func = slice(8, -4)

print(website1[slice_func])
print(website2[slice_func])

# if elif else---------------

name = 'Antony'

if name == 'Debora':
    print('Hi Debora!')
elif name == 'George':
    print('Hi George!')
else:
    print('Who are you?')

age = int(input("Enter the age of your brother: "))

print("kid" if age < 18 else "adult")

# logical operators (and, or, not) - to check two or more conditions are true or not
# -----------------------------------------------------------------------------------

# while loop

name = ""

while len(name) == 0:
    name = input("Enter your name :")

print("Welcome " + name + "!!")
