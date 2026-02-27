def sumar_digitos(n):
    # Función que suma los dígitos de un número y repite el proceso hasta que el resultado sea de un solo dígito
    while n >= 10:
        n = sum(int(digito) for digito in str(n))
    return n

def transformar_n(n, k):
    # Transformar el número n, k veces según las reglas del problema
    n = list(str(n))  # Convertir el número en una lista de caracteres (dígitos)
    
    for _ in range(k):
        # Paso b1: sumar los dígitos de n y reducir a un dígito si es necesario
        suma = sumar_digitos(int(''.join(n)))
        
        # Paso b2: eliminar el último dígito de n
        n.pop()
        
        # Paso b3: insertar la suma al principio del número
        n.insert(0, str(suma))
    
    # Retornar el número final como cadena
    return ''.join(n)

# Leer la cantidad de casos de prueba
cantidad_casos = int(input())

# Procesar cada caso de prueba
for _ in range(cantidad_casos):
    # Leer los valores de n y k para cada caso
    n, k = map(int, input().split())
    
    # Aplicar la transformación al número n k veces
    resultado = transformar_n(n, k)
    
    # Imprimir el resultado
    print(resultado)

    