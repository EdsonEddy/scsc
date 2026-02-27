import sys

input = sys.stdin.read
data = input().split()

num_casos = int(data[0])
index = 1

resultados = []

for _ in range(num_casos):
	n = data[index]
	k = int(data[index + 1])
	index += 2

	for _ in range(k):
		suma = sum(int(digit) for digit in n)
		while suma >= 10:
			suma = sum(int(digit) for digit in str(suma))
		n = n[:-1]
		n = str(suma) + n
	resultados.append(n)

for resultado in resultados:
	print(resultado)