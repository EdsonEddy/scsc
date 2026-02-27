def digital_root(x, k):
    if x == 0:
        return 0
    m = x % 9
    if m == 0:
        return 9
    else:
        r = pow(m, k, 9)
        if r == 0:
            return 9
        else:
            return r

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    index = 1
    for _ in range(n):
        x = int(data[index])
        k = int(data[index +1])
        index +=2
        dr = digital_root(x, k)
        print(dr)

if __name__ == "__main__":
    main()
