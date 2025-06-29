from typing import List
import bisect

class Solution:
    @staticmethod
    def fast_pow(a: int, b: int, mod: int):
        result = 1
        a %= mod
        
        while b > 0:
            if b % 2 == 1:
                result = (result * a) % mod
            a = (a * a) % mod
            b //= 2
            
        return result
    
    def numSubseq(self, nums: List[int], target: int) -> int:
        res = 0
        mod = 10 ** 9 + 7
        nums.sort()
        n = len(nums)
        
        for i in range(n):
            if nums[i] * 2 > target:
                break
            
            j = bisect.bisect_right(nums, target - nums[i]) - 1
            if j >= i:
                add_res = self.fast_pow(2, j - i, 10 ** 9 + 7)
                res = (res + add_res) % mod
            
        return res
    
def main():
    nums = [3, 5, 6, 7]
    target = 9
    sol = Solution()
    print(sol.numSubseq(nums, target))

if __name__ == "__main__":
    main()