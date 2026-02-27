#Ejercicio B --> Suma Recursiva

#Casos de prueba
t = int(input())

for _ in range(t):
    #Datos de entrada
    x, k = map(int, input().split())
    n = x

    if n == 0:
        root_x = 0
    else:
        root_x = 1 + (n - 1) % 9

    power = root_x ** k
    n = power

    if n == 0:
        result = 0
    else:
        result = 1 + (n - 1) % 9

    print(result)
