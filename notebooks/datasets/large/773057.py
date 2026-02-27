n = int(input())
for _ in range(n):
	a = int(input())
	if a==1:
		print(1)
		continue
	else:
		print(f"{(a-1)**3}+{a**3}")
		