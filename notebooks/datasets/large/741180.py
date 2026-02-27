def round_java_style(number):
    return int(number + 0.5)
def calcular_porcentajes(cadena):
    total_caracteres = len(cadena)
    conteo_vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for char in cadena:
        if char in conteo_vocales:
            conteo_vocales[char] += 1

    resultados = []
    for vocal in 'aeiou':
        if total_caracteres > 0:
            porcentaje = (conteo_vocales[vocal] / total_caracteres) * 100
            porcentaje_redondeado = round_java_style(porcentaje * 100) / 100.0
            resultados.append(f"{vocal}= {porcentaje_redondeado:.2f}")
        else:
            resultados.append(f"{vocal}= 0.00")
    
    return resultados
T = int(input())
for caso in range(T):
    S = input().strip()
    print(f"Caso {caso + 1}:")
    porcentajes = calcular_porcentajes(S)
    for resultado in porcentajes:
        print(resultado)