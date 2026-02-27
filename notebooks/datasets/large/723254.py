
def sumarDigitos(n):
    aux = 0
    while(n>0):
        aux = (n%10)+aux
        n = n//10
    return aux

x = int(input())
for i in range(x):
    n,k = map(int, input().split())
    numD = len(str(n)) -1
    for j in range(k):
        sumD = sumarDigitos(n)
        while(len(str(sumD))>1):
            sumD=sumarDigitos(sumD)
        n = n//10
        j = (10**numD) * sumD
        n = j+n
    print(n)



