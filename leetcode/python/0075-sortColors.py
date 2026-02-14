from typing import List

class Solution:  
    def sortColors(self, nums: List[int]) -> None:
        zeros, ptr, twos = 0, 0, len(nums) - 1
        while ptr <= twos:
            if nums[ptr] == 0:
                nums[ptr], nums[zeros] = nums[zeros], nums[ptr]
                zeros += 1
                ptr += 1
            elif nums[ptr] == 2:
                nums[ptr], nums[twos] = nums[twos], nums[ptr]
                twos -= 1
            else:
                ptr += 1

def main():
    nums = [2, 0, 2, 1, 1, 0]
    Solution().sortColors(nums)
    print(nums)

if __name__ == "__main__":
    main()
