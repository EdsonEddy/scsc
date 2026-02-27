def raiz_digital(n):
    if n == 0:
        return 0
    return 1 + (n - 1) % 9
def resolver():
    t = int(input())
    for _ in range(t):
        x, k = map(int, input().split())
        xk = x ** k
        resultado = raiz_digital(xk)
        print(resultado)
resolver()
