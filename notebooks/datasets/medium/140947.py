while True:
	n = int(input())
	if n==-1:
		break
	print(n,'= ',end='')
	i = 2
	f, c, sw = [], 0, 0
	while i * i <= n:
		if n % i!=0:
			i += 1
		else:
			n //= i
			f.append(i)
	if n > 1:
		f.append(n)
	f.append(0)
	lim = len(f)
	while c < lim:
		if f[c] == 0:
			print('')
			break
		if sw == 0:
			if f.count(f[c])>1:
				print(f[c],'^',f.count(f[c]),sep='',end='')
				c=c+f.count(f[c])
				sw=sw+1
			else:
				print(f[c],end='')
				c=c+1
				sw=sw+1
		else:
			if f.count(f[c])>1:
					print('*',f[c],'^',f.count(f[c]),sep='',end='')
					c=c+f.count(f[c])
			else:
				print('*',f[c],sep='',end='')
				c=c+1