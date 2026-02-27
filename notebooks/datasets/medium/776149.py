def descomponer_en_primos(n):
    if n == 1:
        return "1 = 1"
    
    factores = {}
    num = n

    while num % 2 == 0:
        factores[2] = factores.get(2, 0) + 1
        num = num // 2

    i = 3
    max_factor = int(num**0.5) + 1
    while i <= max_factor:
        while num % i == 0:
            factores[i] = factores.get(i, 0) + 1
            num = num // i
            max_factor = int(num**0.5) + 1
        i += 2

    if num > 1:
        factores[num] = factores.get(num, 0) + 1
    
    resultado = f"{n} = "
    primos_ordenados = sorted(factores.keys())
    elementos = []
    for primo in primos_ordenados:
        if factores[primo] == 1:
            elementos.append(str(primo))
        else:
            elementos.append(f"{primo}^{factores[primo]}")
    
    return resultado + "*".join(elementos)

def main():
    import sys
    for linea in sys.stdin:
        n = int(linea.strip())
        if n == -1:
            break
        print(descomponer_en_primos(n))

if __name__ == '__main__':
    main()