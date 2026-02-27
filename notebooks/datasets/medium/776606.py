from sys import stdin
 
lim = 1000005
num = [True] * lim
num[0] = num[1] = False
prim = []
for i in range(2, lim):
    if num[i]:
        prim.append(i)
        for j in range(i * i, lim, i):
            num[j] = False
 
for linea in stdin:
    n = int(linea.strip())
    if n == -1:
        break  

    aux = n
    answ = []
 
    for p in prim:
        if p * p > n:
            break
        cont = 0
        while n % p == 0:
            n //= p
            cont += 1
        if cont == 1:
            answ.append(str(p))
        elif cont > 1:
            answ.append(f"{p}^{cont}")
    if n > 1:
        answ.append(str(n)) 
    print(f"{aux} = ", end="")
    print(*answ,sep="*")