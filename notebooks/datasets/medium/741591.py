def digital_root(n):
    """Calcula el dígito raíz de un número n."""
    if n == 0:
        return 0
    else:
        return 1 + (n - 1) % 9
 
def a201_value(x, k):
    """Calcula el valor de a201 para un par (x, k)."""
    # Calcula x^k
    num = x ** k
    
    # Encuentra el dígito raíz del número resultante
    return digital_root(num)
 
def main():
    # Leer el número de casos de prueba
    t = int(input())
    
    results = []
    # Leer cada caso de prueba
    for _ in range(t):
        x, k = map(int, input().split())
        # Calcular el valor de a201 para el caso actual
        result = a201_value(x, k)
        # Almacenar el resultado
        results.append(result)
    
    # Imprimir todos los resultados
    for res in results:
        print(res)
 
# Llamar a la función principal
if __name__ == "__main__":
    main()