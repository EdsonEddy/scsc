import math
def esprimo(n):
    if n < 2:
        return False
    limite = int(math.isqrt(n))
    for divisor in range(2, limite + 1):
        if n % divisor == 0:
            return False
    return True

casos = int(input().strip())
for _ in range(casos):
    c = int(input().strip())
    max = 0
    for i in range(1, 501):
        conteo = 0
        n = i
        while n <= 500:
            valor = n * n - n + c
            if esprimo(valor):
                conteo += 1
                n += 1
            else:
                break
        if conteo > max:
            max = conteo
    print(f"{c}: {max}")