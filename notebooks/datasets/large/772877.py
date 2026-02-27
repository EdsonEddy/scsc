T = int(input())  # Número de casos de prueba

for _ in range(T):
    n = int(input())  # Número a evaluar
    if n == 1:
        print("1")
    else:
        resultado = f"{(n-1)**3}+{n**3}"
        print(resultado)