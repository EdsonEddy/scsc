def primo(v):
    if v < 2:
        return False
    if v == 2:
        return True
    if v % 2 == 0:
        return False
    for i in range(3, int(v**(1/2)) + 1, 2):
        if v % i == 0:
            return False
    return True

c = int(input())

for _ in range(c):
    k = int(input())
    mx = 0
    actual = 0
    
    for n in range(1, 501):
        m = n * n - n + k
        if primo(m):
            actual += 1
        else:
            if actual > mx:
                mx = actual
            actual = 0
    
    if actual > mx:
        mx = actual
    
    print(f"{k}: {mx}")
