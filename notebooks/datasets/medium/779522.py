import sys 
def fibo(n):
    lista=[1,2]
    i=0
    while True:        
        k=lista[i]+lista[i+1]
        if k>n:
            break
        lista.append(k)
        i+=1
    return(lista)

for file in sys.stdin:
    n=int(file.strip())
    lista=fibo(n)
    lista=lista[::-1]
    nueva_lista=[]
    for j in range(len(lista)):
        if n>=lista[j]:
            nueva_lista.append(1)
            n=n-lista[j]
        else:
            nueva_lista.append(0)
    nlista="".join(str(k)for k in nueva_lista)
    print(nlista)