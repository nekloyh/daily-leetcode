from typing import List

class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0

        def check_nums_pair(needed: int, threshold: int) -> bool:
            cnt = 0
            i = 0
            while i < len(nums) - 1:
                if nums[i + 1] - nums[i] <= threshold:
                    cnt += 1
                    i += 2  
                else:
                    i += 1
            return cnt >= needed
        
        nums.sort()
        lf, rg = 0, nums[-1] - nums[0]
        
        res = rg
        while lf <= rg:
            mid = (rg - lf) // 2 + lf
            if check_nums_pair(p, threshold=mid):
                res = mid
                rg = mid - 1
            else:
                lf = mid + 1
                
        return res
                
        
def main():
    nums = [4, 2, 1, 2]
    p = 1
    sol = Solution()
    print(sol.minimizeMax(nums, p))

if __name__ == "__main__":
    main()
    