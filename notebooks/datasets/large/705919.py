def calcular_sucesion(n):
    if n == 1:
        return "1"
    else:
        cubo_anterior = (n - 1) ** 3
        cubo_actual = n ** 3
        return f"{cubo_anterior}+{cubo_actual}"

T = int(input())

for _ in range(T):
    n = int(input())
    print(calcular_sucesion(n))