T = int(input())
cubes = [i**3 for i in range(1, 102)]
for _ in range(T):
    n = int(input())
    if n == 1:
        print(cubes[0])
    else:
        print(f"{cubes[n-2]}+{cubes[n-1]}")