import math
n = int(input())
for _ in range(n):
    a, b = map(int, input().strip().split())    
    tiempo_optimizar = 0   
    while tiempo_optimizar < a:
        nuevo_tiempo = math.ceil(b / (tiempo_optimizar + 1))
        if nuevo_tiempo <= a - tiempo_optimizar:
            print("si")
            break       
        tiempo_optimizar += 1     
    else:      
        print("no")
