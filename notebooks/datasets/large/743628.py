import math
def cumplirplazo(plazo, demora):
    dias = 0
    while dias < plazo:
        tiempo_restante = demora / (dias + 1)
        if math.ceil(tiempo_restante) <= (plazo - dias):
            return "si"
        dias+= 1
    return "no"
n = int(input())
resultados = []
for _ in range(n):
    plazo, demora = map(int, input().split())
    resultados.append(cumplirplazo(plazo, demora))
for resultado in resultados:
    print(resultado)
