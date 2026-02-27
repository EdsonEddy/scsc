def check_divisible_by_7(n):
    original_remainder = n % 7
    steps = []
    current = n
    while current > 81:
        last_digit = current % 10
        remaining = current // 10
        steps.append((remaining, last_digit))
        current = remaining + last_digit * 5
    final_remainder = current % 7
    correct = (final_remainder == original_remainder)
    return steps, current, correct

t = int(input())
for _ in range(t):
    n = int(input())
    steps, final_num, correct = check_divisible_by_7(n)
    output = ''.join([f"({a}, {b})" for a, b in steps])
    output += f" {final_num} {'correcto' if correct else 'incorrecto'}"
    print(output)