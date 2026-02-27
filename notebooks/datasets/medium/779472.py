from sys import stdin

fibo=[1,2]

for i in range(60):
    fibo.append(fibo[-1]+fibo[-2])

for linea in stdin:
    n=int(linea.strip())

    resp=[0]*60

    for i in range(len(fibo)-1,-1,-1):
        if n>=fibo[i]:
            resp[i]=1
            n-=fibo[i]

    resp=resp[::-1]
    pos=resp.index(1)

    print(*resp[pos:],sep="")