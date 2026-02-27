def sumar_digitos(n):
    """Función para sumar los dígitos de un número hasta obtener un solo dígito"""
    while n >= 10:
        suma = 0
        while n > 0:
            suma += n % 10
            n //= 10
        n = suma
    return n

def transformar_numero(n, k):
    """Función que aplica el proceso k veces sobre el número n"""
    n = str(n)
    for _ in range(k):
        # Paso b1: sumar los dígitos de n y reducirlo a un solo dígito
        suma = sumar_digitos(int(n))
        
        # Paso b2: eliminar el último dígito de n
        n = n[:-1]
        
        # Paso b3: insertar la suma al principio del número
        n = str(suma) + n
    
    return n

# Leer la cantidad de casos de prueba
casos = int(input())

# Procesar cada caso de prueba
for _ in range(casos):
    # Leer n y k
    n, k = map(int, input().split())
    
    # Transformar el número n k veces
    resultado = transformar_numero(n, k)
    
    # Imprimir el resultado final
    print(resultado)
