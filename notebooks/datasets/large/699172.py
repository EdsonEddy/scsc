a, b = map(int, input().split())
n = [int(x) for x in input().split()]
r = sum(x for x in n if a <= x <= b)
print(r)
