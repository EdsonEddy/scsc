T = int(input().strip())
for _ in range(T):
    n = int(input().strip())
    if n == 1:
        print("1")
    else:
        num1 = (n - 1) ** 3
        num2 = n ** 3
        print(f"{num1}+{num2}")