def count_places(city, x, y, visited, i, j):
    
    if i < 0 or i >= x or j < 0 or j >= y or city[i][j] == '#' or visited[i][j]:
        return 0
    
    
    visited[i][j] = True
    
    
    count = 1  
    count += count_places(city, x, y, visited, i + 1, j)  
    count += count_places(city, x, y, visited, i - 1, j)  
    count += count_places(city, x, y, visited, i, j + 1)  
    count += count_places(city, x, y, visited, i, j - 1)  
    
    return count

def main():
    while True:
        
        x, y = map(int, input().split())
        if x == 0 and y == 0:
            break
        
        city = [input().strip() for _ in range(x)]
        
        
        start_i = start_j = -1
        for i in range(x):
            for j in range(y):
                if city[i][j] == '@':
                    start_i, start_j = i, j
                    break
            if start_i != -1:
                break
        
        
        visited = [[False] * y for _ in range(x)]
        
        
        result = count_places(city, x, y, visited, start_i, start_j)
        
        print(result)

if __name__ == "__main__":
    main()
