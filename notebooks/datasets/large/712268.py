def sum_of_digits(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

def process_number(n, k):
    n_str = str(n)
    for _ in range(k):
        digit_sum = sum_of_digits(int(n_str))
        n_str = str(digit_sum) + n_str[:-1]
    return n_str

def main():
    num_cases = int(input().strip())
    results = []

    for _ in range(num_cases):
        n, k = map(int, input().strip().split())
        result = process_number(n, k)
        results.append(result)

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
