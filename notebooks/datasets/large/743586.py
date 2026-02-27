import math

def verificar_plazo_entrega(casos_de_prueba):
    resultados = []
    
    for plazo, tiempo in casos_de_prueba:
        dias_optimizacion = 0
        es_posible = False
        
      
        while plazo > 0:
   
            tiempo_optimizado = math.ceil(tiempo / (dias_optimizacion + 1))
            if tiempo_optimizado <= plazo:
                es_posible = True
                break
            dias_optimizacion += 1
            plazo -= 1
        
        resultados.append("si" if es_posible else "no")
    
    return resultados


n = int(input())
casos_de_prueba = []

for _ in range(n):
    plazo, tiempo = map(int, input().split())
    casos_de_prueba.append((plazo, tiempo))

resultados = verificar_plazo_entrega(casos_de_prueba)
for resultado in resultados:
    print(resultado)