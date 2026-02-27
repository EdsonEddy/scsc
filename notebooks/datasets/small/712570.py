from collections import deque
def contar_lugares_accesibles(m, fi, ci):
    f = len(m)
    c = len(m[0])
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    co = deque([(fi, ci)])
    vis = set()
    vis.add((fi, ci))
    cont = 0
    while co:
        F, C = co.popleft()
        cont += 1
        for d_f, d_c in d:
            NF, NC = F + d_f, C + d_c
            if (0 <= NF < f and 0 <= NC < c and
                m[NF][NC] == '.' and
                (NF, NC) not in vis):
                vis.add((NF, NC))
                co.append((NF, NC))
    return cont
def main():
    while True:
        x, y = map(int, input().strip().split())
        if x == 0 and y == 0:
            break
        m = [input().strip() for _ in range(x)]
        for i in range(x):
            if '@' in m[i]:
                fi = i
                ci = m[i].index('@')
                break
        r = contar_lugares_accesibles(m, fi, ci)
        print(r)
if __name__ == "__main__":
    main()