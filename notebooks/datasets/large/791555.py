import math

# Función para redondear un número a dos decimales
def round2(n):
    return math.floor(n * 100 + 0.5) / 100

T = int(input())  # Leer el número de casos de prueba

for _ in range(T):
    cadena = input().lower()  # Leer la cadena y convertirla a minúsculas
    a = cadena.count("a")     # Contar las 'a'
    e = cadena.count("e")     # Contar las 'e'
    i = cadena.count("i")     # Contar las 'i'
    o = cadena.count("o")     # Contar las 'o'
    u = cadena.count("u")     # Contar las 'u'
    total = len(cadena) - cadena.count(" ")  # Calcular el total de letras (sin espacios)
    print("Caso {0}:".format(_ + 1))         # Imprimir el número de caso
    # Imprimir el porcentaje de cada vocal, redondeado a dos decimales
    print("a=", "{0:.2f}".format(round2((a * 100) / total)))
    print("e=", "{0:.2f}".format(round2((e * 100) / total)))
    print("i=", "{0:.2f}".format(round2((i * 100) / total)))
    print("o=", "{0:.2f}".format(round2((o * 100) / total)))
    print("u=", "{0:.2f}".format(round2((u * 100) / total)))
