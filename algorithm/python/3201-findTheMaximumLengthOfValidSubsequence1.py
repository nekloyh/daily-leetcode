from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        odd, even = 0, 0
        fi_odd, fi_even = 0, 0
        for num in nums:
            if num % 2 == 0:
                even += 1
                if fi_odd % 2 == 1:
                    fi_odd += 1
                if fi_even % 2 == 0:
                    fi_even += 1
            else:
                odd += 1
                if fi_odd % 2 == 0:
                    fi_odd += 1
                if fi_even % 2 == 1:
                    fi_even += 1
        return max(odd, even, fi_odd, fi_even)
        
    
def main():
    sol = Solution()
    nums = [1, 2, 1, 1, 2, 1, 2]
    print(sol.maximumLength(nums))
    
if __name__ == "__main__":
    main()