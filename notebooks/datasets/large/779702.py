def calcular_suma_cubos(n):
    if n == 1:
        return 1
    cubo_n = (n -1) ** 3
    cubo_n1 = n  ** 3
    return f"{cubo_n}+{cubo_n1}"

# Solicitar la cantidad de casos de prueba
T = int(input())

# Procesar cada caso de prueba
for _ in range(T):
    n = int(input())
    resultado = calcular_suma_cubos(n)
    print(resultado)