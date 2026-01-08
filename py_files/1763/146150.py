def GenerarPrim(x):
    UltimoNumeroP=2
    i=UltimoNumeroP
    numeros=[True,True]+[True]*(x-1)
    while UltimoNumeroP**2 <=x:
        i+=UltimoNumeroP
        while i <= x:
            numeros[i]=False
            i+=UltimoNumeroP
        j=UltimoNumeroP+1
        while j<x:
            if numeros[j]:
              UltimoNumeroP=j
              break
            j+=1
        i=UltimoNumeroP
    return [ i+2 for i,z in enumerate(numeros[2:]) if z]
j=GenerarPrim(10000)
casos=int(input())
while casos >0:
    casos=casos-1
    k=int(input())
    lu=[]
    for n in range(0,len(j)):
        y=k*2**n+1
        if y in j:
            lu.append(y)
    if len(lu)==0:
        print(-1)
    else:
        print(lu[0])