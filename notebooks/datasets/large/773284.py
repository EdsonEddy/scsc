def calcular_resultado(n):
    a = (n - 1) ** 3
    b = n ** 3
    return f"{a}+{b}"

T = int(input())

for _ in range(T):
    n = int(input())
    if n == 1:
        print("1")
    else:
        print(calcular_resultado(n))