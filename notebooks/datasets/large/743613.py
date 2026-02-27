def es_posible_cumplir(plazo, demora):
    dias_restantes = plazo
    tiempo_optimizando = 0
    
    while dias_restantes > 0:
        tiempo_actual = (demora + (tiempo_optimizando + 1) - 1) // (tiempo_optimizando + 1)
        
        if tiempo_actual <= dias_restantes:
            return True
            
        dias_restantes -= 1
        tiempo_optimizando += 1
        
    return False

n = int(input())
for _ in range(n):
    plazo, demora = map(int, input().split())
    if es_posible_cumplir(plazo, demora):
        print("si")
    else:
        print("no")