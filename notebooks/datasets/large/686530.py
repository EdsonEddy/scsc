# Desproporción Diagonal

x=int(input())
for i in range(x):
    n=int(input())
    s1=0; s2=0
    v=[]
    for i in range(n):
        l=list(map(int, input().strip()))
        v.append(l)
    m=len(v)
    for i in range(m):
        s1=s1+v[i][i]
        s2=s2+v[i][n-i-1]
    d=s1-s2
    print(d)

