t = int(input())
for _ in range(t):
    n = input()
    original_mod = int(n) % 7
    steps = []
    while int(n) > 81:
        a, b = n[:-1], n[-1]
        steps.append(f"({a}, {b})")
        n = str(int(a) + int(b) * 5)
    final = int(n)
    result = "correcto" if final % 7 == original_mod else "incorrecto"
    print(''.join(steps), final, result)
