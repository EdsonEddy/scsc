import sys
sys.setrecursionlimit(10000)
def dfs(ciudad,x,y,visited,filas,columnas):
	if x<0 or x>=filas or y<0 or y>=columnas or visited[x][y] or ciudad[x][y]=='#':
		return 0
	visited[x][y]=True
	count=1
	movimientos=[(-1,0),(1,0),(0,-1),(0,1)]
	for dx,dy in movimientos:
		count+=dfs(ciudad,x+dx,y+dy,visited,filas,columnas)
	return count

def solve():
	while True:
		x,y=map(int, input().split())
		if x==0 and y==0:
			break
		ciudad=[list(input().strip()) for _ in range(x)]
	
		inicio_x,inicio_y=-1,-1
		for i in range(x):
			for j in range(y):
				if ciudad[i][j]=='@':
					inicio_x,inicio_y=i,j
					break
			if inicio_x!=-1:
				break
		
		visited=[[False for _ in range(y)] for _ in range(x)]
		answer=dfs(ciudad,inicio_x,inicio_y,visited,x,y)
		print(answer)
solve()
