def java_round(x):
    return int(x + 0.5) if x >= 0 else int(x - 0.5)
 
def solve():
    import sys
    input = sys.stdin.read().split('\n')
    T = int(input[0])
    for case in range(1, T+1):
        s = input[case].strip()
        total = len(s)
        vowels = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
        for c in s:
            if c in vowels:
                vowels[c] += 1
        print(f"Caso {case}:")
        for v in sorted(vowels):
            pct = vowels[v] * 100 / total if total else 0
            rounded = java_round(pct * 100) / 100
            print(f"{v}= {rounded:.2f}")
 
solve()