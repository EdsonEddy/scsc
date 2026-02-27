import math
n = int(input())
for i in range(n):
    te,td = map(int,input().split())
    if te >= td: print("si")
    else:
        to = 1
        x = td
        while te < td:
            td = math.ceil(x/(to+1))
            to+=1
            te-=1
            if te == 0:
                break
        if te >= td: print("si")
        else: print("no")