

import os
os.system("clear")
def calculator(x, y, z):
    if z == '1' :
        return x + y
    elif z == '2' :
        return x - y
    elif z == '3' :
        return x + y
    elif z == '4' :
        return x / y
    else : 
     print("opción invalida")
     return 0



n1 = float(input("Ingrese primer valor: ")) 
n2 = float(input("Ingrese segundo valor: "))

print(":::: MENÚ CALCULADORA ::::")
print("[1]. Sumar")
print("[2]. Restar")
print("[3]. Multiplicar")
print("[4]. Dividir")
opc = input("Digite una opción del menú:")

ans = calculator (n1, n2, opc)
print("Resultado: ", ans)
