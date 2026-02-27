for i in range(int(input())):
	n = int(input())
	if(n==1):
		print(1)
	else:
		n=n-1
		print(f"{n**3}+{(n+1)**3}")