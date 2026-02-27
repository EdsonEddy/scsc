import math


def puede_cumplir(plazo, tiempo):
	dias_optimizar = 0

	while dias_optimizar < plazo:
		tiempo_reducido = math.ceil(tiempo / (dias_optimizar + 1))
		if tiempo_reducido <= plazo - dias_optimizar:
			return "si"
		dias_optimizar += 1

	return "no"


def main():
	n = int(input())
	for _ in range(n):
		plazo, tiempo = map(int, input().split())
		resultado = puede_cumplir(plazo, tiempo)
		print(resultado)


if __name__ == "__main__":
	main()