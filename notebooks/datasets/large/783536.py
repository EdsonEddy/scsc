import math

def es_primo(x):
    if x < 2:
        return False
    l = int(math.isqrt(x))
    for d in range(2, l + 1):
        if x % d == 0:
            return False
    return True

t = int(input().strip())
for _ in range(t):
    c = int(input().strip())
    max_c = 0
    for i in range(1, 501):
        cnt = 0
        n = i
        while n <= 500:
            val = n * n - n + c
            if es_primo(val):
                cnt += 1
                n += 1
            else:
                break
        if cnt > max_c:
            max_c = cnt
    print(f"{c}: {max_c}")