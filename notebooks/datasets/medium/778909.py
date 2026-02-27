def fibonacci_base_representation(n):
    fibonacci = [1, 2]
    while fibonacci[-1] <= n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    if fibonacci[-1] > n:
        fibonacci.pop()
    result = []
    for f in fibonacci[::-1]:
        if n >= f:
            result.append('1')
            n -= f
        else:
            result.append('0')
    return ''.join(result)
import sys
input = sys.stdin.read
data = input().splitlines()
for line in data:
    if line.strip():
        number = int(line.strip())
        print(fibonacci_base_representation(number))
