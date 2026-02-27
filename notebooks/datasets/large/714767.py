def suma_digitos(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

def transformar_numero(n, k):
    n_str = str(n)
    for _ in range(k):
        suma = suma_digitos(int(n_str))
        n_str = str(suma) + n_str[:-1]
    return int(n_str)
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    resultado = transformar_numero(n, k)
    print(resultado)