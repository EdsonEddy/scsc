import heapq


def minimum_addition_cost(numbers):
    heapq.heapify(numbers)
    total_cost = 0

    while len(numbers) > 1:
        first = heapq.heappop(numbers)
        second = heapq.heappop(numbers)
        cost = first + second
        total_cost += cost
        heapq.heappush(numbers, cost)

    return total_cost


def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    index = 0
    while index < len(data):
        n = int(data[index])
        index += 1
        if n == 0:
            break

        numbers = list(map(int, data[index:index + n]))
        index += n

        result = minimum_addition_cost(numbers)
        print(result)


if __name__ == "__main__":
    main()
