# Función para obtener la suma de los dígitos hasta que quede un solo dígito
def suma_digitos_unica(n):
    while n >= 10:
        n = sum(int(digito) for digito in str(n))
    return n

# Leer el número de casos de prueba
t = int(input())

# Procesar cada caso de prueba
for _ in range(t):
    n, k = input().split()
    n = int(n)
    k = int(k)

    for _ in range(k):
        suma = suma_digitos_unica(n)
        
        n = n // 10
        
        n = int(str(suma) + str(n))
    
    print(n)
