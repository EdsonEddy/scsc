res = []
for _ in range(int(input())):
    n = int(input())
    res.append(f'{(n-1)**3}+{n**3}' if n != 1 else '1')

for i in res: print(i)