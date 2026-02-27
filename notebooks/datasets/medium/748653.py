import heapq

def min_cost_sum():
    while True:
        n = int(input())
        if n == 0:
            break
            
        # Read the numbers and create a min heap
        numbers = list(map(int, input().split()))
        heapq.heapify(numbers)
        
        total_cost = 0
        # Keep combining the two smallest numbers until only one remains
        while len(numbers) > 1:
            # Get the two smallest numbers
            a = heapq.heappop(numbers)
            b = heapq.heappop(numbers)
            
            # Calculate current sum
            current_sum = a + b
            # Add to total cost
            total_cost += current_sum
            # Push the sum back to the heap
            heapq.heappush(numbers, current_sum)
            
        print(total_cost)

if __name__ == "__main__":
    min_cost_sum()