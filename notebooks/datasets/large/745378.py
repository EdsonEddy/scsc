import math
n = int(input().strip())
for _ in range(n):
    te,td = map(int, input().strip().split())
    if te >= td:
        print("si")
    else:
        to = 1
        x = td
        while te < td and te > 0:
            td = (x + to) // (to + 1)
            to += 1
            te -= 1
        if te >= td:
            print("si")
        else:
            print("no")