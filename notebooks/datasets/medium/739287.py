def reduccion_digital(n):
    # Función para encontrar la reducción digital (dígito raíz)
    if n == 0:
        return 0
    return 1 + (n - 1) % 9

# Leer número de casos de prueba
for _ in range(int(input())):
    # Leer x y k, aplicar la reducción digital para x^k
    x, k = map(int, input().split())
    
    # Calcular la reducción digital del número x elevado a la potencia k
    resultado = reduccion_digital(reduccion_digital(x) ** k)
    
    # Imprimir el resultado final
    print(resultado)
