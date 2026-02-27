def cribar_primos(limite):
    # Crear una lista booleana que marque los números primos
    es_primo = [True] * (limite + 1)
    es_primo[0] = es_primo[1] = False  # Sabemos que 0 y 1 no son primos
    for i in range(2, int(limite**0.5) + 1):
        if es_primo[i]:
            for j in range(i * i, limite + 1, i):
                es_primo[j] = False
    primos = [i for i in range(2, limite + 1) if es_primo[i]]
    return primos

def descomponer_en_factores(n, primos):
    factores = []
    for primo in primos:
        if primo * primo > n:
            break
        while n % primo == 0:
            factores.append(primo)
            n //= primo
    if n > 1:
        factores.append(n)
    return factores

def imprimir_factores(n, factores):
    contador = {}
    for f in factores:
        if f in contador:
            contador[f] += 1
        else:
            contador[f] = 1
    
    resultado = []
    for factor, exp in sorted(contador.items()):
        if exp > 1:
            resultado.append(f"{factor}^{exp}")
        else:
            resultado.append(str(factor))
    
    return f"{n} = {'*'.join(resultado)}"

def main():
    limite = 1000000
    primos = cribar_primos(limite)
    
    while True:
        n = int(input())
        if n == -1:
            break
        factores = descomponer_en_factores(n, primos)
        print(imprimir_factores(n, factores))

if __name__ == "__main__":
    main()