import math
def poscum(plz, dem):
    for top in range(plz):
        tre = math.ceil(dem / (top + 1))
        if tre <= (plz - top):
            return "si"
    return "no"
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(poscum(a, b))