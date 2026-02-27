import heapq


def min_cost(nums):
    nums = [num for num in nums]
    
    heapq.heapify(nums)
    cost = 0
    while len(nums) > 1:
        smallest = heapq.heappop(nums)
        second_smallest = heapq.heappop(nums)

        cost += smallest + second_smallest
        heapq.heappush(nums, smallest + second_smallest)

    return cost


def main():
    t_c = int(input())
    while t_c != 0:
        l_nums = list(map(int, input().split()))
        minimus = min_cost(l_nums)
        print(minimus)
        t_c = int(input())


if __name__ == '__main__':
    main()