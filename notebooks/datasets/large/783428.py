import sys
import math

def is_prime(x):
    if x < 2:
        return False
    if x % 2 == 0:
        return x == 2
    r = int(math.sqrt(x))
    for i in range(3, r + 1, 2):
        if x % i == 0:
            return False
    return True

data = sys.stdin.read().strip().split()
if not data:
    exit()
t = int(data[0])
idx = 1
for _ in range(t):
    k = int(data[idx])
    idx += 1
    maxi = 0
    for start in range(1, 501):
        count = 0
        for n in range(start, 501):
            val = n * n - n + k
            if is_prime(val):
                count += 1
            else:
                break
        if count > maxi:
            maxi = count
    sys.stdout.write(f"{k}: {maxi}\n")
