def raiz_digital(n):
    if n == 0:
        return 0
    elif n % 9 == 0:
        return 9
    else:
        return n % 9

def suma_recursiva(x, k):
    # Calculamos x^k
    numero = x ** k
    # Retornamos la raíz digital
    return raiz_digital(numero)

# Lectura de la entrada
n = int(input())
for _ in range(n):
    x, k = map(int, input().split())
    print(suma_recursiva(x, k))
