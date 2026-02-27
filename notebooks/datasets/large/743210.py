import math
def optimizar(plazo,demora):
    posible=True
    for i in range(demora):
        t_entrega=i+math.ceil(demora/(i+1))
        if t_entrega<=plazo:
            posible=False
    return posible
    
casos=int(input())
for j in range(casos):
    plazo, demora= map(int,input().split())
    if optimizar(plazo,demora)==False:
        print("si")
    else:
        print("no")