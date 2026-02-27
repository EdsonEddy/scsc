import heapq

def min_cost_sum(numbers):
    heapq.heapify(numbers)  # Create a min-heap for efficient sorting
    total_cost = 0

    while len(numbers) > 1:
        num1 = heapq.heappop(numbers)  # Get the two smallest numbers
        num2 = heapq.heappop(numbers)
        cost = num1 + num2
        total_cost += cost
        heapq.heappush(numbers, cost)  # Push the sum back into the heap

    return total_cost

# Read input cases until N is 0
while True:
    N = int(input())
    if N == 0:
        break

    numbers = list(map(int, input().split()))  # Read the numbers
    min_cost = min_cost_sum(numbers)
    print(min_cost)
