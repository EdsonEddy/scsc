def calcular_sucesion(n):
    base_inicio = 1
    suma_anterior = 0
    resultado = []
    for i in range(1, n + 1):
    
        num_elementos = 2 * i - 1
        suma_actual = sum(range(base_inicio, base_inicio + num_elementos))
        potencia_actual = i ** 3
        
        if i == 1: 
            resultado.append("1")
        else:
            resultado.append(f"{suma_anterior}+{potencia_actual}")
        
        base_inicio += num_elementos
        suma_anterior = potencia_actual
    return resultado

T = int(input(""))
numeros = []
for _ in range(T):
    numeros.append(int(input()))

for n in numeros:
    resultados = calcular_sucesion(n)
    print(resultados[n - 1])
