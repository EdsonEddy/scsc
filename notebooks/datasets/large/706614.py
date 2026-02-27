def generar_secuencia_cubos(max_n):
    cubos = [i**3 for i in range(1, max_n + 2)]  # Calcula cubos desde 1^3 hasta (max_n+1)^3
    return cubos

# Leer número de casos de prueba
T = int(input())

# Generar los cubos necesarios
max_n = 100
cubos = generar_secuencia_cubos(max_n)

# Procesar cada caso de prueba
for _ in range(T):
    n = int(input())
    if n == 1:
        print(cubos[0])
    else:
        print(f"{cubos[n-2]}+{cubos[n-1]}")
