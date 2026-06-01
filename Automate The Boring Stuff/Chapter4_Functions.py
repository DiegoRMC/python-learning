# Chapter 4 - Functions

# Creating our first function:
def hello():
    print ("hello")

# The previous function does not use a parameter, in order to make the function use one:
def hey(name):
    print('hey ' + name + '!')

hey('diego')

# Return:
import random

def respuesta(r):
    if r == 1:
        return "Está claro"
    elif r == 2:
        return "El tiempo lo dirá"
    elif r == 3:
        return "Jamás"

input("Qué deseas saber? : ")
print(respuesta(random.randint(1, 3)))

# The None value (es lo mismo que el null)
# Las funciones sin return statement devuelven siempre un None

# You can also name parameters when creating functions so they don't are just used by the order you put the 
# arguments in, this can be useful to create optional parameters, the print() function for example has the end parameter
print('Hello', end='') # If we add this it will no longer put a new line at the end 
print('World')

# When you pass it various arguments separed by commas, it will automatically add an space between them
print('cats', 'dogs', 'mice')
# But when we specify the sep parameter...
print('cats', 'dogs', 'mice', sep=',')
# This means by default the sep parameter is set to ' '
# We will learn how to add this feature to our functions later in the book

# The Call Stack:

# Esto simplemente significa que cuando tu llamas a una función a mitad de código al terminar la función el código se seguirá ejecutando desde donde estaba

# Local / Global Scope

# Es simplemente pillar la lógica del call stack, todo lo que esté dentro de algo es local, y lo de arriba es global para el, mostly

# Este código es interesante porque da error pese a haber una variable global declarada llamada eggs, como es global deberías poder usar el pirnt sin fallo
# pero Python hace algo curioso que es decidir que las variables son locales o globales antes de ejecutar el código, por ello, en el contexto de esa función
# eggs es siempre una variable local que todavía no ha sido asignada, lo cual lleva a error

def spam():
    print(eggs)  # ERROR!
    eggs = 'spam local'
   
eggs = 'global'
spam()

# Exception Handling

# Esto es para que los errores no siempre hagan que el código se deje de ejecutar, por ejemplo aquí el código de try se ejecutará
# y al detectar un error saltará directo al código del except
# NOTA: El except solo se ejecuta si el error que salta es el que pones de argumento y si te salta otro error al de tu argumento se parará la ejecucion como si no huebiera nada

def spam(divide_by):
    try:
        # Any code in this block that causes ZeroDivisionError won't crash the program:
        return 42 / divide_by
    except ZeroDivisionError:
        # If ZeroDivisionError happened, the code in this block runs:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

# Ejemplo bubbles

import time, sys, random

input("Press anything to start hacking (hasta el infinito): ")
try:
    while True:

        print(random.randint(0,1), end=' ')
        time.sleep(1/random.randint(10,100))
    
except KeyboardInterrupt:
    print("\nProceso interrumpido")
    sys.exit()

# ejercicio
import random

def get_random_dice_roll():
    return diceroll

for i in range(4):
    diceroll = random.randint(1,6)
    print(get_random_dice_roll())

# Collatz

def collatz(n):
        if (n%2) == 0:
            n = n // 2
            return n
        else:
            n = 3*n+1
            return n

try:
    numero_a_jugar = int(input("Escribe un número entero para reducir a 1 con collatz: "))
    print (numero_a_jugar, end=" ")
    while numero_a_jugar != 1:
        print(collatz(numero_a_jugar), end=" ")
        numero_a_jugar = collatz(numero_a_jugar)

except ValueError:
    print("Eso no es un número colgao")