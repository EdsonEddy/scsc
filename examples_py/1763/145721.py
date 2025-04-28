import math

def primo(numerito):
    if numerito < 2:
        return False
    for i in range(2,int(math.sqrt(numerito)+1)):
        if  numerito % i == 0:
            return False
    return True

lim = 10**4
casitos = int(input())
for x in range(casitos):
    k = int(input())
    n = 0
    res = k * 2 ** (n) + 1
    while not primo(res):
        n += 1
        res = k * 2**(n) + 1
    if res < lim:
        print(res)
    else:
        print(-1)