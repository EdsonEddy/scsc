import heapq

def min_addition_cost(nums):
    
    heapq.heapify(nums)
    
    
    total_cost = 0
    
    
    while len(nums) > 1:
        
        first = heapq.heappop(nums)
        second = heapq.heappop(nums)
        
        
        current_sum = first + second
        total_cost += current_sum
        
        
        heapq.heappush(nums, current_sum)
    
    return total_cost


while True:
    
    N = int(input())
    
    
    if N == 0:
        break
    
    
    nums = list(map(int, input().split()))
    
    
    print(min_addition_cost(nums))