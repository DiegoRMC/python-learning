# Chapter two (if, else and flow control):

# Some boolean stuff (en Python son True y False, con mayúscula)
calvo = False
print (40 == 40.0) # Pese a ser distinto tipo de variable, esto es True, de ser una string uno de ellos sería False
# Luego tenemos los miticos AND, OR, NOT

# Flow Control
# Some if else I already know, in Python if else need : before the block they will exectute
# Tenemos también elif, que es lo mismo que else if en sql server
# Es clave saber que un elif terminará tu if siempre que sea true

# Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.
spam = 2

if int(spam) == 1:
    print ("Hello")
elif int(spam) == 2:
    print ("Howdy")
else:
    print ("Greetings!")