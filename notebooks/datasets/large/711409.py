def digit_sum(n):
	while n >= 10:
		n = sum(int(digit) for digit in str(n))
	return n


def process_case(n, k):
	n = str(n)
	for _ in range(k):
		sum_digits = digit_sum(sum(int(digit) for digit in n))
		n = n[:-1]
		n = str(sum_digits) + n
	return n


def main():
	import sys
	input = sys.stdin.read
	data = input().strip().split('\n')

	num_cases = int(data[0].strip())
	results = []

	for i in range(1, num_cases + 1):
		n, k = map(int, data[i].strip().split())
		result = process_case(n, k)
		results.append(result)

	for result in results:
		print(result)


if __name__ == "__main__":
	main()
