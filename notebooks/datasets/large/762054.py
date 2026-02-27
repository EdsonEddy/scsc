def java_round(number, decimals=2):

    factor = 10 ** decimals
    return int(number * factor + (0.5 if number >= 0 else -0.5)) / factor

def calcular_porcentajes(jardin):
    # Inicializar contadores para cada vocal
    total = len(jardin)
    conteo = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    # Contar vocales
    for c in jardin:
        if c in conteo:
            conteo[c] += 1
    
    # Imprimir resultados
    for vocal in ['a', 'e', 'i', 'o', 'u']:
        if total == 0:
            porcentaje = 0.0
        else:
            porcentaje = java_round((conteo[vocal] * 100.0) / total)
        print(f"{vocal}= {porcentaje:.2f}")

def main():
    T = int(input())
    for caso in range(1, T + 1):
        jardin = input().strip()
        print(f"Caso {caso}:")
        calcular_porcentajes(jardin)

if __name__ == "__main__":
    main()