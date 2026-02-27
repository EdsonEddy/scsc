def s(n):
    return sum(int(d) for d in str(n))
def a201(x, k):
    n = pow(x, k, 9)  
    n = s(n)
    for _ in range(200):
        n = s(n)
    return n if n != 0 else 9
def resolver_casos():
    casos = int(input())
    resultados = []
    
    for _ in range(casos):
        x, k = map(int, input().split())
        resultado = a201(x, k)
        resultados.append(resultado)
    
    for resultado in resultados:
        print(resultado)
while True:
    try:
        resolver_casos()
    except EOFError:
        break
