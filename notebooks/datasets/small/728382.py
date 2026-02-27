from collections import deque
def Paseando(m, f, c, vis):
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    def dfs(x, y):
        if (x, y) in vis:
            return 0
        vis.add((x, y))
        count = 1
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(m) and 0 <= ny < len(m[0]) and m[nx][ny] == '.':
                count += dfs(nx, ny)
        return count

    return dfs(f, c)

while True:
    x, y = map(int, input().strip().split())
    if x == 0 and y == 0:
        break
    m = [input().strip() for _ in range(x)]
    fi, ci = -1, -1
    for i in range(x):
        if '@' in m[i]:
            fi, ci = i, m[i].index('@')
            break
    if fi != -1 and ci != -1:
        vis = set()
        r = Paseando(m, fi, ci, vis)
        print(r)