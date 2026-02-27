while(True):
	n = int(input())
	if(n==-1):break
	v = {}
	print(n,'=',end=' ')
	while(n%2==0):
		if(2 in v):v[2] += 1
		else:v[2] = 1
		n = n//2
	i = 3
	while(i*i<=n):
		while(n%i==0):
			if(i in v):v[i] += 1
			else:v[i] = 1
			n = n//i
		i += 2
	if(n>1):
		if(n in v):v[n] += 1
		else:v[n] = 1
	sw = 1
	for i in v:
		#print(i,v[i])
		if sw :
			sw = 0			
			if(v[i]==1):
				print(str(i),end='')
			else:
				print(str(i)+'^'+str(v[i]),end='')
		elif(v[i]==1):
			print('*'+str(i),end='')
		else:
			print('*'+str(i)+'^'+str(v[i]),end='')
	print()
