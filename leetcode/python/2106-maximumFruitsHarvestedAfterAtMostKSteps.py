class Solution:
    def maxTotalFruits(self, fruits, startPos: int, k: int) -> int:
        left = total = res = 0
        for right in range(len(fruits)):
            total += fruits[right][1]
            while left <= right and fruits[right][0] - fruits[left][0] + min(abs(startPos - fruits[left][0]), 
                                                                             abs(startPos - fruits[right][0])) > k:
                total -= fruits[left][1]
                left += 1
            res = max(res, total)
        return res
    
def main():
    sol = Solution()
    fruits = [[2, 8], [6, 3], [8, 6]]
    startPos = 5
    k = 4
    print(sol.maxTotalFruits(fruits, startPos, k))
    
if __name__ == "__main__":
    main()
    