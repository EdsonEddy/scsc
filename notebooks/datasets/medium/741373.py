
def calcular_suma_digitos(numero):
    suma = 0
    for digito in str(numero):
        suma += int(digito)
    return suma


def obtener_digito_repetitivo(numero):
    if numero == 0:
        return 0
    else:
        return 1 + (numero - 1) % 9


cantidad_casos = int(input())


for _ in range(cantidad_casos):
    
    x, k = map(int, input().split())
    
    
    resultado_numero = x ** k
    
   
    digito_final = obtener_digito_repetitivo(resultado_numero)
    
    
    print(digito_final)
