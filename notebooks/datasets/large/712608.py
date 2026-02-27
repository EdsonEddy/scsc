def digit_sum(num):
    """Calcula la suma de los dígitos de un número y reduce a un solo dígito si es necesario."""
    while num >= 10:
        num = sum(int(digit) for digit in str(num))
    return num


def process_number(n, k):
    """Realiza las operaciones descritas en el problema k veces sobre el número n."""
    n = str(n)
    for _ in range(k):

        sum_digit = digit_sum(sum(int(digit) for digit in n))


        n = n[:-1]


        n = str(sum_digit) + n

    return n


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