import heapq
import sys
def calcmn(entrada):
    res = []
    while True:
        n = int(entrada.pop(0))
        if n == 0:
            break
        nums = list(map(int, entrada[:n]))
        entrada = entrada[n:]
        heapq.heapify(nums)
        tot_cst = 0
        while len(nums) > 1:
            num1 = heapq.heappop(nums)
            num2 = heapq.heappop(nums)
            cst_act = num1 + num2
            tot_cst += cst_act
            heapq.heappush(nums, cst_act)
        res.append(tot_cst)
    return res
def main():
    inp_txt = sys.stdin.read()
    entrada = inp_txt.split()
    res = calcmn(entrada)
    for r in res:
        print(r)
if __name__ == "__main__":
    main()
