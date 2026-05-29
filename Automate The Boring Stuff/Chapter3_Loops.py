# Chapter 3 - Loops

# While loops:

while True: # Infinite loop, that's why we use break
    print('Please type your name.')
    name = input('>')
    if name == 'your name':
        break
print('Thank you!')

# If you get stuck in an infinite loop just press CTRL-C

while True:
    print('Who are you?')
    name = input('>')
    if name != 'Diego':
      continue      # Como no eres Diego te devuelve al principio del loop
    print('Hello, Diego. What is the password? (It is a fish.)')
    password = input('>')
    if password == 'swordfish':
        break
print('Access granted.')

# Apparently other data type and value combinations can also be True o False, this is called Truthy of Falsey
print(bool(0)) # The bool function tells you. int 0, float 0.0 and string '' are all False

# For loops and the range() function:
# Some cool example (you can also use break and continue in these)
print('Hello!')
for i in range(5):
    print('On this iteration, i is set to ' + str(i))
print('Goodbye!')

# Code para Gauss (suma nums del 1 al 100, rollo 1+2+3+4...)
total = 0
for i in range(101):
    total = total + i
print (total)
# More arguments on range(), with two you specify starting and end value (well not really the end one, would be 15 here)
for i in range(12, 16):
    print(i)
for i in range(0, 10, 2): #With 3 you specify the step argument
    print(i)

# Importing our first modules (librerias vaya)
import random, sys, os, math

# Un ejemplo de uso de random

for i in range(5):
    print(random.randint(1, 10)) # Fun fact, random si te incluye 1 y 10 en su rango, lmao

# Otra que es muy útil y nos sirve como flow control es sys.exit()

import sys

while True:
    n = int(input("Presiona 1 para cerrar el programa, 2 para printear Hola 7 veces  >>> "))
    if n == 1:
        sys.exit()
    elif n == 2:
        for i in range(7):
            print('Hola')
        break
    else:
        print('Que haces bro')

# Crea un guess the number, va

import random

n = random.randint(1,100)
guess = 0
intentos = 0

while guess != n:
    guess = int(input("Introduce tu guess: "))
    
    if guess < n:
        print("Too low")
        intentos = intentos + 1
        continue
    else:
        print ("Too high")
        intentos = intentos + 1
        continue
if intentos <= 7: 
    print("Lo has logrado en " + str(intentos) + ", ni tan mal.")
else:
    print("Lo has hecho en " + str(intentos) + ", eres bastante malo...")


# 1 to 10 with while
n = 1
while n != 11:
    print(n)
    n = n + 1

# 1 to 10 with for
for i in range (1, 11):
    print(i)