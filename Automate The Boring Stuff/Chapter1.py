# Operators:

# Exponentiation:
print (2 ** 8)
# Resto:
print (8 % 2)
# Integer division (same as normal division but result is rounded down)
print (9 // 4)

# Variables (Data types)
# Tenemos a los clásicos, int, float y str
# int / int = float
# int + int = int
# int + float = float

# We also have concatenation of strings using + and replication using *
print ('calvo ' * 6)

# Variables
nombre = 'diego'
print (nombre)
# Naming restrictions on variables:
# No spaces, only letters, numbers and underscores(_), can't begin with number, can't be a python keyword (if, return, for)

# This program says hello and asks for my name.

print('Hello, world!')
print('What is your name?')  # Ask for their name.
my_name = input('>')
print('It is good to meet you, ' + my_name)
print('The length of your name is: ' + str(len(my_name)))
print('What is your age?')  # Ask for their age.
my_age = input('>')
print('You will be ' + str(int(my_age) + 1) + ' in a year.')

# The input() function always returns a string
# This does not work:
n = input()
n2 = n + 4
print (n2)

# The int() function can be used to round down a float value

# Useful functions:
type (n)
len(my_name)
abs(n)
print (round(7.555, 2)) # Valor a redondear y número de

