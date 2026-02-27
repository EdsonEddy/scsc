from sys import *
for line in stdin:
    a,b=map(int,line.split())
    v=input().split()
    s=0
    for i in range(len(v)):
        if(a<=int(v[i])and int(v[i])<=b):
            s=s+int(v[i])
    print(s)
