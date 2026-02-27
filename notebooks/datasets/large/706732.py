def cubo_perfecto(n):
    return n ** 3

def suma_consecutivos(n):
    if n == 1:
        return "1"
    else:
        suma_anterior = int((n - 1) ** 3)
        cubo_perfecto_n = cubo_perfecto(n)
        return f"{suma_anterior}+{cubo_perfecto_n}"

t = int(input())
for _ in range(t):
    n = int(input())
    print(suma_consecutivos(n))