'''Crear una calculadora que reciba dos valores
por consola, y realice las operaciones aritméticas básicas'''

import os ## IMPORTAR BILBLIOTECA LIBRERIA 
# randind  genera numero aliatorio enteros en un rango especificado por el desarrollador 
from random import randint, uniform

os.system('clear') ## EJECUTAR COMANDOS DE SISTEMA OPERATIVO

#inputs
print("Ingrese primer valor: ")
n1 = int(input())
n2 = int(input("Ingrese el segundo valor: \n"))
suma = n1 + n2
print("Suma:", suma)

print(type(n1))