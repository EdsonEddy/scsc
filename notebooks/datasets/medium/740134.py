def suma_digitos(n):
    return sum(int(d) for d in str(n))
def digito_raiz(n):
    if n == 0:
        return 0
    return 1 + (n - 1) % 9
def resolver_casos(casos):
    for x, k in casos:
        num = x ** k
        print(digito_raiz(num))
n = int(input())  
casos = [tuple(map(int, input().split())) for _ in range(n)]
resolver_casos(casos)