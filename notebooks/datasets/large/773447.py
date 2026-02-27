T = int(input())

for _ in range(T):
    n = int(input())
    if n == 1:
        print("1")
    else:
        cubo_1 = (n - 1) ** 3
        cubo_2 = n ** 3
        print(f"{cubo_1}+{cubo_2}")
