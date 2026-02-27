def sum_of_digits(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

t = int(input())
for _ in range(t):
    n, k = input().split()
    n = list(n)
    k = int(k)

    for _ in range(k):
        digit_sum = sum_of_digits(int(''.join(n)))
        n.pop()
        n.insert(0, str(digit_sum))

    print(''.join(n))
