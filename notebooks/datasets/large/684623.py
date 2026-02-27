num_cases = int(input())

for _ in range(num_cases):
    n = int(input())
    matrix = [input() for _ in range(n)]
    
    diag1 = sum(int(matrix[i][i]) for i in range(n))
    diag2 = sum(int(matrix[i][n - 1 - i]) for i in range(n))
    
    print(diag1 - diag2)
