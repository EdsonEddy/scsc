import heapq

def process_heap_operations():
    while True:
        n = int(input().strip())
        if n <= 0:
            break

        elements = list(map(int, input().strip().split()))
        heapq.heapify(elements)

        total_cost = 0
        while len(elements) > 1:
            first_min = heapq.heappop(elements)
            second_min = heapq.heappop(elements)
            combined_cost = first_min + second_min
            total_cost += combined_cost
            heapq.heappush(elements, combined_cost)

        print(total_cost)

if __name__ == "__main__":
    process_heap_operations()
