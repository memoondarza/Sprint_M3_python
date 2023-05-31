"""
sample () es una función incorporada del módulo aleatorio en Python que devuelve 
una lista de longitud particular de elementos elegidos de una secuencia, es decir, una lista, tupla, cadena o conjunto.
"""

# Importamos el método sample de random.
from random import sample

# Declaramos la función con un argumento (longitud de la contraseña)
def password_generator(longitud):
  
    # Definimos los caracteres y simbolos
    
    abc_minusculas = "abcdefghijklmnopqrstuvwxyz"
    
    # HACK: upper() transforma las letras de una cadena en mayusculas
    abc_mayusculas = abc_minusculas.upper() 
    
    numeros = "0123456789"
    #simbolos = "{}[]()*;/,_-"
    
    # Definimos la secuencia
    secuencia = abc_minusculas + abc_mayusculas + numeros
    
    # Llamamos la función sample() utilizando la secuencia, y la longitud
    password_union = sample(secuencia, longitud)
    
    # Con join insertamos los elementos de una lista en una cadena
    password_result = "".join(password_union)
    
    # Retornamos la variables "password_result"
    return password_result
