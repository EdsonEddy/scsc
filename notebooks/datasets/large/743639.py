import math

def p(n, c):
    r = []
    
    for a, b in c:
        p = a
        d = b
        o = 0
        
        while o < p:
            t = math.ceil(d / (o + 1))
            if t <= p - o:
                r.append("si")
                break
            o += 1
        else:
            r.append("no")
    
    return r

n = int(input())
c = [tuple(map(int, input().split())) for _ in range(n)]

r = p(n, c)
for res in r:
    print(res)
