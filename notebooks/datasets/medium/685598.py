import heapq

def minimal_addition_cost(cases):
    results = []
    
    for numbers in cases:
        if len(numbers) == 0:
            continue
        
        heapq.heapify(numbers)
        total_cost = 0
        
        while len(numbers) > 1:
            first_min = heapq.heappop(numbers)
            second_min = heapq.heappop(numbers)
            cost = first_min + second_min
            total_cost += cost
            heapq.heappush(numbers, cost)
        
        results.append(total_cost)
    
    return results

import sys
input = sys.stdin.read
data = input().split()

index = 0
cases = []

while index < len(data):
    n = int(data[index])
    index += 1
    if n == 0:
        break
    numbers = list(map(int, data[index:index + n]))
    index += n
    cases.append(numbers)

results = minimal_addition_cost(cases)

for result in results:
    print(result)
