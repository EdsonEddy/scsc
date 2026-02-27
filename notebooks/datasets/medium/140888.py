
def esprimo(n):
    if n == 1:
        return False
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def prime_factores(n):
    prime_factor_list = []
    while not n % 2:
        prime_factor_list.append(2)
        n //= 2
    while not n % 3:
        prime_factor_list.append(3)
        n //= 3
    i = 5
    while n != 1:
        if esprimo(i):
            while not n % i:
                prime_factor_list.append(i)
                n //= i
        i += 2

    return prime_factor_list
def frecuencia(lista):
	y='^'
	esp='*'
	cava=''
	slista = set(lista)
	slista=sorted(slista, key=float)
	for i in slista:
		t=lista.count(i)
		if t==1:
			t=str(t)
			i=str(i)
			cava=cava+i+esp
			
		else:
			t=str(t)
			i=str(i)
			cava=cava+i+y+t+esp
	return str(cava)
nn=int(input())
while nn!=-1:
	jj=prime_factores(nn)
	ig='='
	gh=frecuencia(jj)
	print(nn,ig,gh[:len(gh)-1])
	nn=int(input())	
