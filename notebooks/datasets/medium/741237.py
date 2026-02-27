# Función para obtener la suma de los dígitos de un número (aunque no se utiliza en el resultado final)
def calcular_suma_digitos(num):
    return sum(int(digito) for digito in str(num))

# Función para calcular el dígito raíz
def obtener_digito_raiz(num):
    if num == 0:
        return 0
    else:
        return 1 + (num - 1) % 9

# Leer la cantidad de casos de prueba
casos = int(input())

# Procesar cada caso de prueba
for _ in range(casos):
    # Leer los valores de x y k
    x, k = map(int, input().split())
    
    # Elevar x a la potencia de k
    potencia = x ** k
    
    # Calcular el dígito raíz
    digito_final = obtener_digito_raiz(potencia)
    
    # Mostrar el resultado
    print(digito_final)