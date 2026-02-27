def calcular_resultado(n):
    # Definir los números cúbicos iniciales
    cubos = [1]
    i = 2
    while len(cubos) < n + 1:
        cubos.append(i ** 3)
        i += 1
    
    # Determinar los números que corresponden al resultado para el índice n
    if n == 1:
        return "1"
    else:
        return f"{cubos[n - 2]}+{cubos[n - 1]}"

# Leer el número de casos de prueba
T = int(input().strip())

# Procesar cada caso de prueba
for _ in range(T):
    n = int(input().strip())
    print(calcular_resultado(n))