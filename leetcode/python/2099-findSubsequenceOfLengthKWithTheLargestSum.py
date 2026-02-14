from typing import List

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        n_nums = [(num, i) for i, num in enumerate(nums)]
        n_nums.sort(key=lambda x: -x[0])
        k_nums = sorted(n_nums[:k], key=lambda x: x[1])
        return [num for num, _ in k_nums]    
    
def main():
    nums = [2, 1, 3, 3]
    k = 2
    sol = Solution()
    print(sol.maxSubsequence(nums, k))
    
if __name__ == "__main__":
    main()