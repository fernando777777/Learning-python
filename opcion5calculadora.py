import os
os.system("clear")

def calculator(x, y, z):
    if z == '1':
        return x + y
    elif z == '2':
        return x - y
    elif z == '3':
        return x * y
    elif z == '4':
        if y == 0:
            return 'No es posible dividir entre cero'
        else:
            return x / y
    else:
        print("Opción invalida")
        return 0

n1 = float(input("Ingrese primer valor: "))
n2 = float(input("Ingrese segundo valor: "))

print(":::: MENÚ CALCULADORA ::::")
print("[1]. Sumar")
print("[2]. Restar")
print("[3]. Multiplicar")
print("[4]. Dividir")
print("[5]. Todas las operaciones")
opc = input("Digite una opción del menú:")

if opc == '5':
    print("Resultado Suma: ", calculator(n1, n2, '1'))
    print("Resultado Resta: ", calculator(n1, n2, '2'))
    print("Resultado Multiplicación: ", calculator(n1, n2, '3'))
    print("Resultado División: ", calculator(n1, n2, '4'))
else:
    ans = calculator(n1, n2, opc)
    print("Resultado: ", ans)