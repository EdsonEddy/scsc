def puede_cumplir_plazo(plazo, demora):
    if demora <= plazo:
        return True
    
    for dias_optimizando in range(1, plazo):
        nuevo_tiempo = (demora + dias_optimizando + 1 - 1) // (dias_optimizando + 1)
        tiempo_disponible = plazo - dias_optimizando
        
        if nuevo_tiempo <= tiempo_disponible:
            return True
    
    return False

def procesar_casos():
    n = int(input())
    
    for _ in range(n):
        plazo, demora = map(int, input().split())
        
        if puede_cumplir_plazo(plazo, demora):
            print("si")
        else:
            print("no")

procesar_casos()
