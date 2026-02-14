from typing import List

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        res = []
        r = 0
        n = len(nums)
        for j in range(n):
            if nums[j] == key:
                l = max(r, j - k) # noqa: E741
                r = min(n - 1, j + k) + 1
                for i in range(l, r):
                    res.append(i)
        return res
            
def main():
    sol = Solution()
    nums = [3, 4, 9, 1, 3, 9, 5]
    key = 9
    k = 1
    print(sol.findKDistantIndices(nums, key, k))

if __name__ == "__main__":
    main()