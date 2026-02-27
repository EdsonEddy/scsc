def primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

t = int(input())
for _ in range(t):
    c = int(input())
    maxc = 0
    cnt = 0
    for i in range(1, 501):
        if primo(i*i - i + c):
            cnt += 1
        else:
            if cnt > maxc:
                maxc = cnt
            cnt = 0
    if cnt > maxc:
        maxc = cnt
    print(f"{c}: {maxc}")