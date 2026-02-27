def calculate_next_sum(n):
    # Calcular el cubo del número n
    current_cubic = n ** 3
    # Calcular el cubo del número n-1
    previous_cubic = (n - 1) ** 3
    # Solo se imprime el siguiente cubo si el cubo anterior es 0
    if previous_cubic == 0:
        return f"{current_cubic}"
    else:
        return f"{previous_cubic}+{current_cubic}"

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        n = int(data[i])
        result = calculate_next_sum(n)
        results.append(result)
    
    print("\n".join(results))

if __name__ == "__main__":
    main()