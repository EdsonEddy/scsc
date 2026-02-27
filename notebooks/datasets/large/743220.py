import math
def optimizar(t,o):
    opti = math.ceil(t / (o + 1)) 
    return opti

for _ in range(int(input())):

    a,b = map(int, input().split())
    respald = b

    for i in range(1,a+1):
        if a >= b:
            print('si')
            break
        else:
            b = respald
            b = optimizar(b,i)
            a -= 1

    if b > a:
        print('no')

