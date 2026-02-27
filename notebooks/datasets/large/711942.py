def suma_digitos(n):
    """Suma los dígitos de un número hasta obtener una suma con un solo dígito"""
    suma = sum(int(digito) for digito in str(n))
    while suma >= 10:
        suma = sum(int(digito) for digito in str(suma))
    return suma

def eliminar_ultimo_digito(n):
    """Elimina el último dígito de un número"""
    return int(str(n)[:-1])

def insertar_suma_al_principio(n, suma):
    """Inserta la suma al principio de un número"""
    return int(str(suma) + str(n))

def procesar_numero(n, k):
    """Procesa un número según las reglas del problema"""
    for _ in range(k):
        suma = suma_digitos(n)
        n = eliminar_ultimo_digito(n)
        n = insertar_suma_al_principio(n, suma)
    return n

# Leer la cantidad de casos de prueba
num_casos = int(input())

# Procesar cada caso de prueba
for _ in range(num_casos):
    n, k = map(int, input().split())
    resultado = procesar_numero(n, k)
    print(resultado)