#tEntrega
import math
def eP(p, d):
    for o in range(p + 1):
        tR = d / (o + 1)
        if math.ceil(tR) <= p - o:
            return True
    return False
def main():
    n = int(input())
    for _ in range(n):
        p, d = map(int, input().split())
        if eP(p, d):
            print("si")
        else:
            print("no")
main()