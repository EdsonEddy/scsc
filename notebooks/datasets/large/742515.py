import math

n = int(input())

for i in range(n):
    
    a,b = map(int,input().split())
    
    dias_optimizar = 0
    posible = False
    
    while True:
        # Calcular el tiempo de construcción optimizado
        tiempo_optimizacion = b / (dias_optimizar + 1)
        tiempo_optimizacion_redondeado = math.ceil(tiempo_optimizacion)
        
        # Verificar si se puede cumplir con el plazo
        if tiempo_optimizacion_redondeado <= a - dias_optimizar:
            posible = True
            break
        
        # Incrementar el contador de días de optimización
        dias_optimizar += 1
        
        # Si el tiempo optimizado es mayor que el plazo restante, salir
        if dias_optimizar >= a:
            break
    
    # Resultado para cada caso
    if posible:
        print("si")
    else:
        print("no")