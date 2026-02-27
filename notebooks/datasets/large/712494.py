def sumar_digitos(n):
    """Suma los dígitos de un número hasta que tenga un solo dígito."""
    while n >= 10:  # si la suma tiene más de un dígito
        n = sum(int(d) for d in str(n))
    return n

def realizar_proceso(n, k):
    for _ in range(k):
        suma_dig = sumar_digitos(n)
        n = suma_dig * 10**(len(str(n))-1) + n // 10  # insertar suma y eliminar último dígito
    return n

def resolver_casos(casos):
    resultados = []
    for n, k in casos:
        resultados.append(realizar_proceso(n, k))
    return resultados

# Leer entrada
t = int(input())  # número de casos
casos = [tuple(map(int, input().split())) for _ in range(t)]  # leer los casos de prueba

# Resolver y mostrar los resultados
resultados = resolver_casos(casos)
for resultado in resultados:
    print(resultado)