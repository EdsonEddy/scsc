def redondear(valor):
    """Función para redondear como en Java/C."""
    return int(valor * 100 + 0.5) / 100

def calcular_porcentajes(cultivos):
    total = len(cultivos)
    conteo_vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    for char in cultivos:
        if char in conteo_vocales:
            conteo_vocales[char] += 1
    
    resultados = []
    for vocal in 'aeiou':
        porcentaje = (conteo_vocales[vocal] / total) * 100 if total > 0 else 0
        porcentaje_redondeado = redondear(porcentaje)
        resultados.append(f"{vocal}= {porcentaje_redondeado:.2f}")
    
    return resultados

T = int(input())

for caso in range(1, T + 1):
    cultivos = input().strip()
    porcentajes = calcular_porcentajes(cultivos)
    
    print(f"Caso {caso}:")
    for resultado in porcentajes:
        print(resultado)
