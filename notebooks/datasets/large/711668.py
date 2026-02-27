def suma_digitos(n):
	while n >= 10:
		n = sum(int(d) for d in str(n))
	return n
def prcaso(n, k):
	n = str(n)
	for _ in range(k):
		suma = suma_digitos(int(n))
		n = n[:-1]
		n = str(suma) + n

	return n
t = int(input())
for _ in range(t):
	n, k = map(int, input().split())
	resultado = prcaso(n, k)
	print(resultado)