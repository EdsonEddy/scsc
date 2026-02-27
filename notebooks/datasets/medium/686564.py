def calcular_costo_minimo(numeros):
    numeros.sort()
    costo_total = 0
    while len(numeros) > 1:
        suma = numeros[0] + numeros[1]
        costo_total += suma
        numeros = numeros[2:]
        numeros.append(suma)
        numeros.sort()
    return costo_total

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        numeros = list(map(int, input().split()))
        costo_minimo = calcular_costo_minimo(numeros)
        print(costo_minimo)

if __name__ == "__main__":
    main()
