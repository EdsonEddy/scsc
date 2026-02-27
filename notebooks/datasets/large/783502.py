def es_primo(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

T = int(input())
for _ in range(T):
    c = int(input())
    max_run = 0
    current = 0
    for n in range(1, 501):
        if es_primo(n*n - n + c):
            current += 1
        else:
            if current > max_run:
                max_run = current
            current = 0
    if current > max_run:
        max_run = current
    print(f"{c}: {max_run}")
