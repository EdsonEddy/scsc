#9
from sys import stdin

def fibo(n):
    a=0
    b=1
    s=a+b
    r=[]
    while s<n:
        r.append(s)
        a,b=b,s
        s=a+b
    return r

def f(n):
    v=''
    a1=a[::-1]
    s=0
    for i in range(len(a)):
        if a1[i]+s <= n:
            s+=a1[i]
            v+='1'
        else:
            v+='0'
    return v
r=[]
r=[]
for i in stdin:
    n = int(i.strip())
    a = fibo(n)
    v = f(n)
    r.append(v)
print('\n'.join(r))