import math

def es_primo(numero):
    if numero < 2:
        return False
    limite = int(math.isqrt(numero))
    for divisor in range(2, limite + 1):
        if numero % divisor == 0:
            return False
    return True

cantidad_casos = int(input().strip())
for _ in range(cantidad_casos):
    constante = int(input().strip())
    maximo = 0
    for inicio in range(1, 501):
        conteo = 0
        n = inicio
        while n <= 500:
            valor = n * n - n + constante
            if es_primo(valor):
                conteo += 1
                n += 1
            else:
                break
        if conteo > maximo:
            maximo = conteo
    print(f"{constante}: {maximo}")