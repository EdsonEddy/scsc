def sucesion_consecutivos(n):
    if n == 1:
        return "1"
    a = (n - 1) ** 3
    b = n ** 3
    return str(a) + "+" + str(b)

T = int(input())

for _ in range(T):
    n = int(input())
    resultado = sucesion_consecutivos(n)
    print(resultado)