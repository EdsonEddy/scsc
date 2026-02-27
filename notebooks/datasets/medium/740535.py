# Función para calcular la suma de los dígitos de un número
def suma_digitos(n):
    return sum(int(d) for d in str(n))

# Función para obtener el dígito repetitivo
def digito_repetitivo(n):
    if n == 0:
        return 0
    else:
        return 1 + (n - 1) % 9

# Leer el número de casos de prueba
n = int(input())

# Procesar cada caso de prueba
for _ in range(n):
    # Leer x y k
    x, k = map(int, input().split())
    
    # Calcular x^k
    numero = x ** k
    
    # Calcular el dígito repetitivo
    resultado = digito_repetitivo(numero)
    
    # Imprimir el resultado
    print(resultado)