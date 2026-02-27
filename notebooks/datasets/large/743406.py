import math
def es_posible_cumplir(plazo, demora):
    dias_optimizados=0
    while plazo > 0:
        tiempo_optimizado=math.ceil(demora / (dias_optimizados + 1))
        if tiempo_optimizado <= plazo:
            return "si"
        plazo-=1
        dias_optimizados+=1
    return "no"

n=int(input())
resultados=[]
for _ in range(n):
    plazo, demora=map(int, input().split())
    resultados.append(es_posible_cumplir(plazo, demora))

for resultado in resultados:
    print(resultado)