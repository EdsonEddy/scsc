n = int(input())
for _ in range(n):
    t=int(input())
    if t==1:
        print(1)
    else:
        print(f'{(t-1)**3}+{t**3}')