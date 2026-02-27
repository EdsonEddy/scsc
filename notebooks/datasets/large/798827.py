a,b=map(int,input().split())
lista=list(map(int,input().split()))
sumatoria=0
for elemento in lista:
    if elemento<=b and elemento>=a:
        sumatoria+=elemento
print(sumatoria)