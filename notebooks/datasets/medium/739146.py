def suma_digitos(n):
    return sum(int(d) for d in str(n))

def raiz_digital(n):
    if n == 0:
        return 0
    else:
        return 1 + (n - 1) % 9

def resolver_casos(casos):
    for x, k in casos:
        numero = x ** k
        resultado = raiz_digital(numero)
        print(resultado)

n = int(input())
casos = [tuple(map(int, input().split())) for _ in range(n)]

resolver_casos(casos)

