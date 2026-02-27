import sys

fibs = [1, 2]
while fibs[-1] + fibs[-2] <= 10**12:
    fibs.append(fibs[-1] + fibs[-2])

for line in sys.stdin:
    n = int(line.strip())
    result = ""
    used = False

    for i in range(len(fibs)-1, -1, -1):
        if fibs[i] <= n:
            result += "1"
            n -= fibs[i]
            used = True
        elif used:
            result += "0"

    print(result)