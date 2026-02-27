def suma_digitos(n):
    return sum(int(digito) for digito in str(n))

def raiz_digital(n):
    while n >= 10:
        n = suma_digitos(n)
    return n

def procesar_caso(x, k):
    # Optimizamos el cálculo directo de la raíz digital
    if x == 0:
        return 0
    if x == 1:
        return 1
    
    numero = pow(x, k, 9)  # Usamos módulo 9 para reducir el tamaño del número
    return raiz_digital(numero) if numero != 0 else 9

def resolver():
    n = int(input())
    for _ in range(n):
        x, k = map(int, input().split())
        print(procesar_caso(x, k))

resolver()