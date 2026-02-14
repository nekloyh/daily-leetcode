from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        s = 0
        for i in set(nums):
            if i > 0:
                s += i
        if s == 0:
            return max(nums)
        return s
    
    
def main():
    sol = Solution()
    nums = [1, 2, 3, 4, 5]
    print(sol.maxSum(nums))
    
if __name__ == "__main__":
    main()
    