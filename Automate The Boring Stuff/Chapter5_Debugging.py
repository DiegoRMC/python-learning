# Chapter 5 - Debugging

# Raising exceptions

def box_print(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.') # Es como definir nuestros propios errores para luego mostrar
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2.')

    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

# Para mostrar es tan simple como usar un try except 

try:
    box_print('*', 4, 4)
    box_print('O', 20, 5)
    box_print('x', 1, 3)
    box_print('ZZ', 3, 3)
except Exception as err: # Esto asigna a la variable err Exception
    print('An exception happened: ' + str(err))
try:
    box_print('ZZ', 3, 3)
except Exception as err:
    print('An exception happened: ' + str(err))

# Assertions: Es como un if pero para hacer un check de que el programa está funcionando como es de esperar, rollo 'asegurate de que esta parte del código está devolviendo valores positivos
# Las assertions no se deben usar en código listo para interactuar con el usuario, sólo para proceso de desarrollo, para errores cometidos por usuarios usamos el raise exception, no queremos
# que el programa crashee todo el rato para el usuario

ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
ages.reverse()
assert ages[0] <= ages[-1] # Assertion error

# Logging
# Not so different from using a print that tells you which values the variables are taking
# Actually no, aquí lo clave es, de primeras que tu puedes filtrar por nivel, por ejemplo si lo cambias a level=logging.WARNING solo te mostrará lineas que sean de warning, ignorando las de DEBUG,
# esto un print no lo hace, y luego por razones de logfiles un print no puede, esto si te lo puede transcribir a un archivo para que tu veas, además, usar print te la puede liar porque luego
# vas a tener que quitarlos, y imagine que quitas un print que si era del codigo, o te dejas prints inútiles

import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(' + str(n) + ')')
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(' + str(n) + ')')
    return total

print(factorial(5))

logging.debug('End of program')

# Logfiles: Lo dicho antes, para pasar los logs a un .txt haríamos algo como esto, así que lo dicho, estas lineas grabatelas a fuego y cuando vayas a hacer algo medio serio son imprescindibles

import logging
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')

# Logging levels, básicamente en Python son: DEBUG, INFO, WARNING, ERROR, CRITICAL. El que decide realmente en que categoría cae cada mensaje eres tú, así que 0 dramas

# Si no estás usando tus log messages ahora mismo y no quieres que te salgan en la terminal puedes usar logging.disable, que hará que cualquier log debajo de ella no aparezca al ejecutarse
logging.disable()

# Practica con la debugging tool hecha también

