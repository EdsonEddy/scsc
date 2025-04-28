import sys
primos=[2,3,5,7,11,17,19]
for i in range(23,10000):
    for j in primos:
        if i%j==0:
            break
    else:
        primos.append(i)

casos=int(input())
for n in range(casos):
    k=int(input())
    for i in range(10**4):
        x=k*2**i+1
        if(x in primos):
            print(x)
            break
    else:
        print (-1)
