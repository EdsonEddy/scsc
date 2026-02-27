def suma(n):
    while n >= 10:
        n = sum(map(int, str(n)))
    return n
    
def eli_in(n, k):
    for _ in range(k):
        n = int(str(suma(n))+str(n)[:-1])
    return n 
    
def main():
    i = int(input())
    r = [eli_in(*map(int, input().split())) for _ in range(i)]
    print("\n".join(map(str, r)))
if __name__ == "__main__":
    main()