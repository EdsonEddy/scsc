import math

# Función para redondear al estilo de Java o C
def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier + 0.5) / multiplier

def calcular_porcentajes(T, casos):
    vocales = "aeiou"
    
    resultados = []
    
    for i in range(T):
        S = casos[i]
        total_frutas = len(S)
        conteo_vocales = {vocal: 0 for vocal in vocales}
        
        for char in S:
            if char in conteo_vocales:
                conteo_vocales[char] += 1
        
        resultado = f"Caso {i + 1}:"
        for vocal in vocales:
            porcentaje = (conteo_vocales[vocal] / total_frutas) * 100 if total_frutas > 0 else 0
            porcentaje_redondeado = round_half_up(porcentaje, 2)
            resultado += f"\n{vocal}= {porcentaje_redondeado:.2f}"
        
        resultados.append(resultado)
    
    # Imprimir todos los resultados sin líneas adicionales entre los casos
    print("\n".join(resultados))

# Ejemplo de uso con entradas simuladas
T = int(input())  # Número de casos de prueba
casos = [input().strip() for _ in range(T)]  # Listado de cadenas de cultivos

calcular_porcentajes(T, casos)
