import math

def round2(n):
    return math.floor(n * 100 + 0.5) / 100

T = int(input())

for caso in range(1, T + 1):
    cadena = input().lower()
    total = len(cadena.replace(" ", ""))
    print(f"Caso {caso}:")

    for vocal in "aeiou":
        porcentaje = (cadena.count(vocal) * 100) / total
        print(f"{vocal}= {round2(porcentaje):.2f}")
