def calcular_suma(n):
    if n == 1:
        return "1"
    else:
        primer_termino = (n-1)**3
        segundo_termino = n**3
        return f"{primer_termino}+{segundo_termino}"

# Leer el número de casos de prueba
T = int(input())

# Procesar cada caso de prueba
for _ in range(T):
    n = int(input())
    resultado = calcular_suma(n)
    print(resultado)