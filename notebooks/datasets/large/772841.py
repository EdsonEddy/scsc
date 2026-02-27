def calcular_suma(n):
    cubo_anterior = (n - 1) ** 3
    cubo_actual = n ** 3
    return f"{cubo_anterior}+{cubo_actual}"
T = int(input(""))
for _ in range(T):
    n = int(input(""))
    if n == 1:
        print("1")  
    else:
        print(calcular_suma(n))