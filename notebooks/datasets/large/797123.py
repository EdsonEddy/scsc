def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def contar_primos(k):
    seguidos = 0
    mayor = 0
    for n in range(1, 501):
        valor = n * n - n + k
        if es_primo(valor):
            seguidos += 1
            if seguidos > mayor:
                mayor = seguidos
        else:
            seguidos = 0
    return mayor

# entrada y salida
casos = int(input())
for _ in range(casos):
    k = int(input())
    print(f"{k}: {contar_primos(k)}")