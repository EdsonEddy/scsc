def digito_raiz(n):
    if n==0:
        return 0
    else:
        return 1+(n-1)%9
def procesar_casos(casos):
    resultados=[]
    for x,k in casos:
        numero=x**k
        answer=digito_raiz(numero)
        resultados.append(answer)
    return resultados

n=int(input())
casos=[tuple(map(int,input().split())) for _ in range(n)]
for e in procesar_casos(casos):
    print(e)
