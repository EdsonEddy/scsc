def sum_digits(n):
    """Función para calcular la suma de los dígitos de un número"""
    return sum(int(digit) for digit in str(n))

def raiz_digital(n):
    """Función que calcula la raíz digital de un número usando el método matemático"""
    if n == 0:
        return 0
    return 1 + (n - 1) % 9

def procesar_caso(x, k):
    """Función para procesar un solo caso de prueba"""
    # Calcular x^k
    potencia = x ** k
    # Obtener la raíz digital de la potencia
    resultado = raiz_digital(potencia)
    return resultado

# Entrada de datos
n_casos = int(input())  # Leer número de casos de prueba

for _ in range(n_casos):
    x, k = map(int, input().split())  # Leer x y k para cada caso
    print(procesar_caso(x, k))  # Imprimir el resultado para cada caso
