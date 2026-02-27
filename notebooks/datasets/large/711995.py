def sumar_digitos(numeros):
    return sum(map(int, list(numeros)))

def eliminar_digitos(numero):
    return numero[:-1]

def agregar_digitos(n, digitos):
    return str(n) + digitos

pruebas = int(input())
for i in range(pruebas):
    n, k = input().split(" ")
    num = sumar_digitos(n)
    for _ in range(int(k)):
        while len(str(num)) != 1:
            num = sumar_digitos(str(num))
        nn = agregar_digitos(num, eliminar_digitos(str(n)))
        num = n = nn
    print(n)