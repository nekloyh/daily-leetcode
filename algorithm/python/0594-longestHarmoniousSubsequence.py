from typing import List
from collections import Counter

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        num_dist = Counter(nums)
        num_sorted = sorted(list(set(nums)))

        res = 0
        for i in range(len(num_sorted) - 1):
            if abs(num_sorted[i] - num_sorted[i + 1]) == 1:
                tmp = num_dist.get(num_sorted[i + 1], 0) + num_dist.get(num_sorted[i], 0)
                res = max(res, tmp)
        
        return res
    
def main():
    sol = Solution()
    nums = [1, 3, 2, 2, 5, 2, 3, 7]
    print(sol.findLHS(nums))

if __name__ == "__main__":
    main()