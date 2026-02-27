n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    c = 0
    p = False
    for i in range(a, 0, -1):
        r = (b / (c + 1))
        if r <= i:
            print("si")
            p= True
            break
        c += 1
    if not p:
        print("no")