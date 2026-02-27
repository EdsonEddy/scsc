resultados = []
def encontrar_num(posicion):
    n, sum, ant = 0, 0, 0
    for i in range(posicion):
        c = 2*i + 1
        for j in range(c):
            n += 1
            sum = sum + n    
        p = sum - ant 
        sum = 0
        anterior = ant
        ant = p     
    return f"{anterior}+{p}"    

T = int(input())
for k in range(T):
    posicion = int(input())
    if(posicion == 1):
        resultados.append(1)
    else:
        resultados.append(encontrar_num(posicion))
for resultado in resultados:
    print(resultado)