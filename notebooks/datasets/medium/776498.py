def fp(n):
    if n ==1:
        return "1"
    r=[]
    d=2
    while n>1:
        c=0
        while n%d==0:
            c+=1
            n=n//d
        if c>0:
            if c==1:
                r.append(str(d))
            else:
                r.append(f"{d}^{c}")
        d+=1
    return "*".join(r)

ns=[]
while True:
    x=int(input())
    if x==-1:
        break
    if x>0:
        ns.append(x)

for n in ns:
    if n==1:
        print("1 = 1")
    else:
        print(f"{n} = {fp(n)}")
    