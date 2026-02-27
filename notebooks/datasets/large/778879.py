t = int(input())  

for _ in range(t):
    original = input().strip()
    n = int(original)
    trace = []
    current = n
    while current > 81:
        last_digit = current % 10
        rest = current // 10
        trace.append(f"({rest}, {last_digit})")
        current = rest + 5 * last_digit

    result = current
    
    if result % 7 == n % 7:
        trace.append(f" {result} correcto")
    else:
        trace.append(f" {result} incorrecto")
    
    print(''.join(trace))


