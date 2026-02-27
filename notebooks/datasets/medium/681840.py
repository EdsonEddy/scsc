import heapq

def minimum_addition_cost(numbers):
    heapq.heapify(numbers)  # Convertir la lista de números en un min-heap
    total_cost = 0

    while len(numbers) > 1:
        first_min = heapq.heappop(numbers)
        second_min = heapq.heappop(numbers)
        current_cost = first_min + second_min
        total_cost += current_cost
        heapq.heappush(numbers, current_cost)

    return total_cost

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        numbers = list(map(int, input().split()))
        result = minimum_addition_cost(numbers)
        print(result)

if __name__ == "__main__":
    main()
