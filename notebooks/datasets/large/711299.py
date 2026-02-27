def divisible_by_7(n):
    original_remainder = n % 7
    steps = []
    
    while n > 81:
        last_digit = n % 10
        remaining_digits = n // 10
        n = remaining_digits + last_digit * 5
        steps.append((remaining_digits, last_digit))
    
    result_remainder = n % 7
    correctness = "correcto" if result_remainder == original_remainder else "incorrecto"
    
    return steps, n, correctness
T = int(input())
results = []
for _ in range(T):
    n = int(input())
    steps, final_number, correctness = divisible_by_7(n)
    steps_str = "".join(f"({a}, {b})" for a, b in steps)
    print(f"{steps_str} {final_number} {correctness}")