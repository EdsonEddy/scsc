T = int(input().strip())

cubos = [1]

for i in range(1, 101):
    cubos.append(i**3)

for _ in range(T):

    n = int(input().strip())

    if n == 1:
        print("1")
    else:
        print(f"{cubos[n-1]}+{cubos[n]}")
