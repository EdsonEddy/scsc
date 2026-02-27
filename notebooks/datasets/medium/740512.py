def suma_digitos(n):
    return sum(int(d) for d in str(n))

def digito_repetitivo(n):
    if n == 0:
        return 0
    else:
        return 1 + (n - 1) % 9

n = int(input())

for _ in range(n):
    x, k = map(int, input().split())

    numero = x ** k
    resultado = digito_repetitivo(numero)

    print(resultado)