from math import ceil
def cumple(p:int,d:int):
    for i in range(1,p):
        fun=i+ceil(d/(i+1))
        if fun<=p:
            return True
    return False

t=int(input())
for _ in range(t):
    plazo,demora=map(int,input().split())
    if cumple(plazo,demora):
        print("si")
    else:
        print("no")

