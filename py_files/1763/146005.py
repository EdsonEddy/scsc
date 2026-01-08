def primo(num):
    k=2
    while num%k!=0 and k<=num//2:
        k=k+1
    if k>num//2:
        sw=1
    else:
        sw=0
    return sw
n=int(input())
for i in range(n):
    x=int(input())
    sw=0
    c=0
    formula=0
    while sw==0 and formula<10000:
        formula=x*(2**c)+1
        ver=primo(formula)
        if ver==1:
            sw=1
        c=c+1
    print(formula)