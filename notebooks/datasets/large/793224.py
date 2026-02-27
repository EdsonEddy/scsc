import sys

def round_half_up(n, decimals=0):
    """
    Redondeo tipo Java/C: 2.5 -> 3, 2.45 -> 2.5
    """
    multiplier = 10 ** decimals
    return int(n * multiplier + 0.5) / multiplier

t = int(sys.stdin.readline())

for case in range(1, t + 1):
    s = sys.stdin.readline().strip().lower()
    tot = len(s)
    fru = {v: 0 for v in "aeiou"}  # inicializamos frutas

    # Contar vocales
    for letra in s:
        if letra in fru:
            fru[letra] += 1

    print(f"Caso {case}:")
    for clave in "aeiou":
        porcentaje = fru[clave] / tot * 100
        porcentaje_redondeado = round_half_up(porcentaje, 2)
        print(f"{clave}= {porcentaje_redondeado:.2f}")
