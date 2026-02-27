import heapq
import sys

def minimum_addition_cost(numbers):
    if len(numbers) == 1:
        return 0
    

    heapq.heapify(numbers)
    
    total_cost = 0
    
    while len(numbers) > 1:

        first_min = heapq.heappop(numbers)
        second_min = heapq.heappop(numbers)
        

        cost = first_min + second_min
        total_cost += cost

        heapq.heappush(numbers, cost)
    
    return total_cost

def main():
    input = sys.stdin.read
    data = input().strip().split()
    
    index = 0
    results = []
    
    while index < len(data):
        N = int(data[index])
        index += 1
        
        if N == 0:
            break
        
        numbers = list(map(int, data[index:index + N]))
        index += N
        
        result = minimum_addition_cost(numbers)
        results.append(result)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
