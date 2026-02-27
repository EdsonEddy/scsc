def calcular_a201(x, k):
    """Calcula a201 usando propiedades de modulo 9."""
    # Calculamos x^k mod 9
    if x == 0 and k == 0:
        return 0  # 0^0 es indeterminado, consideramos 0
    if x == 0:
        return 0  # Cualquier número elevado a 0 es 1, así que 0^k es 0
    if k == 0:
        return 1  # x^0 es 1

    # Usamos el método de exponenciación modular
    mod = 9
    resultado = 1
    base = x % mod

    while k > 0:
        if k % 2 == 1:  # Si k es impar
            resultado = (resultado * base) % mod
        base = (base * base) % mod
        k //= 2

    return resultado if resultado != 0 else 9  # Convertir 0 a 9

# Leer el número de casos de prueba
num_casos = int(input())
resultados = []

for _ in range(num_casos):
    x, k = map(int, input().split())
    resultado = calcular_a201(x, k)
    resultados.append(resultado)

# Imprimir los resultados
for res in resultados:
    print(res)
