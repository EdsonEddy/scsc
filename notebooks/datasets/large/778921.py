t=int(input())
for _ in range(t):
    n=input()
    o=int(n)%7
    s=''
    while int(n)>81:
        x=int(n[:-1])
        y=int(n[-1])
        s+='('+str(x)+', '+str(y)+')'
        n=str(x+y*5)
    r=int(n)%7
    print(s,n,'correcto' if r==o else 'incorrecto')
