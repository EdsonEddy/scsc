def raiz_digital(n):
    if n == 0:
        return 0
    return 1 + (n - 1) % 9

def suma_digitos_201(x, k):
    potencia = x ** k
    return raiz_digital(potencia)

t = int(input())  

for _ in range(t):
    x, k = map(int, input().split())
    print(suma_digitos_201(x, k))
