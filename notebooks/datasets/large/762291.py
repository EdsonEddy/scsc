import sys
for i in sys.stdin:
    a,b = map(int,i.split())
    v = [int(x) for x in input().split()]
    suma = 0
    for i in v:
        if(i >= a and i<= b):
            suma += i
    print(suma)
