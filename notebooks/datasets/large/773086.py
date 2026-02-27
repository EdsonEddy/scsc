def calcular_sucesion(n):
    resultado = []
    a = 1  
    for i in range(1, n + 1):
        suma_anterior = sum(resultado) if resultado else 0  
        suma_actual = sum(range(a, a + 2 * i - 1)) 
        cubo = (i ** 3)  
        resultado.append(cubo) 
        a += 2 * i - 1  
    return f"{resultado[-2]}+{resultado[-1]}" if len(resultado) > 1 else f"{resultado[0]}"

T = int(input())
for _ in range(T):
    n = int(input())
    print(calcular_sucesion(n))