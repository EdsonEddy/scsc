
def suma_digitos(n):
    return sum(int(digito) for digito in str(n))

def raiz_digital(n):
    while n >= 10:
        n = suma_digitos(n)
    return n

def potencia_modular(base, exponente, mod):
    resultado = 1
    base = base % mod
    while exponente > 0:
        if (exponente % 2) == 1:
            resultado = (resultado * base) % mod
        exponente = exponente // 2
        base = (base * base) % mod
    return resultado

def procesar_caso(x, k):
    if x == 0:
        return 0
    if x == 1:
        return 1

    numero = potencia_modular(x, k, 9)
    return raiz_digital(numero) if numero != 0 else 9

def resolver():
    n = int(input())
    for _ in range(n):
        x, k = map(int, input().split())
        print(procesar_caso(x, k))

resolver()
