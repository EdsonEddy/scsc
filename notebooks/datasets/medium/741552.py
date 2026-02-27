def calcular_raiz_digital(numero):
    if numero == 0:
        return 0
    return 1 + (numero - 1) % 9
 
def suma_digitos_potencia(base, exponente):
    resultado_potencia = base ** exponente
    return calcular_raiz_digital(resultado_potencia)
 
casos_prueba = int(input())  
 
for _ in range(casos_prueba):
    base, exponente = map(int, input().split())
    print(suma_digitos_potencia(base, exponente))
