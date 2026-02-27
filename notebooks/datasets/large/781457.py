n = int(input())
y = "aeiou"

for j in range(1, n + 1):
    x = input()
    t = len(x)
    d = 100.0 / t
    m = {c: 0.0 for c in y}
    for c in x:
        if c in m:
            m[c] += 1
    print(f"Caso {j}:")
    for c in y:
        print(f"{c}= {m[c] * d + 1e-9:.2f}")
