def calculate_diagonal_disproportion(matrix):
    n = len(matrix)
    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0
    for i in range(n):
        primary_diagonal_sum += int(matrix[i][i])
        secondary_diagonal_sum += int(matrix[i][n - i - 1])
    disproportion = primary_diagonal_sum - secondary_diagonal_sum
    return disproportion
def main():
    test_cases = int(input().strip())
    for _ in range(test_cases):
        n = int(input().strip())
        matrix = [list(map(int, input().strip())) for _ in range(n)]
        disproportion = calculate_diagonal_disproportion(matrix)
        print(disproportion)
if __name__ == "__main__":
    main()
