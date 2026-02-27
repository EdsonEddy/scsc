def raiz_digital(n):
    if n == 0:
        return 0
    return 1 + (n - 1) % 9

def suma_recursiva(x, k):
    # Calculamos x^k usando pow para grandes potencias
    numero = pow(x, k)
    # Calculamos la raíz digital del número obtenido
    return raiz_digital(numero)

# Entrada
casos = int(input())
for _ in range(casos):
    x, k = map(int, input().split())
    print(suma_recursiva(x, k))