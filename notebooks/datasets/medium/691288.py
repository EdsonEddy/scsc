import heapq

def min_cost(arr):
    heapq.heapify(arr)
    res = 0

    while len(arr) > 1:
        first = heapq.heappop(arr)
        second = heapq.heappop(arr)
        sum_val = first + second
        res += sum_val
        heapq.heappush(arr, sum_val)

    return res

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

        arr = []
        for i in range(n):
            arr.append(int(data[index + i]))
        index += n

        print(min_cost(arr))

if __name__ == "__main__":
    main()
