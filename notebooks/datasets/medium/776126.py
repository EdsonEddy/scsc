def f(n):
    r,i={},2
    while i*i<=n:
        while n%i==0:r[i]=r.get(i,0)+1;n//=i
        i+=1
    if n>1:r[n]=1
    return '*'.join(f'{k}^{v}'*(v>1)+f'{k}'*(v==1) for k,v in r.items())    
while (n:=int(input()))+1:
    print(f"{n} = {f(n)}")    