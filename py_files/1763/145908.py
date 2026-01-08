def primo(numero):
    for i in range(2, numero):
        if (numero % i) == 0:
            return False
    return True
cas=int(input())
while cas>0:
    k=int(input())
    l=[]
    for i in range(10**4):
        m=(k*(2**i))+1
        l.append(m)
        if m>10**4:
            break
    for j in range(len(l)):
        res=primo(l[j])
        c=True
        if res==c:
            break
    if res==c:
        print(l[j])
    else:
        print(-1)
    cas-=1