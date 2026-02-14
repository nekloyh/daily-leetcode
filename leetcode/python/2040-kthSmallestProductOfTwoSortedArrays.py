from typing import List
import bisect

class Solution:
    @staticmethod
    def count_pairs(x: int, nums1: List[int], nums2: List[int]) -> int:
        count = 0
        for a in nums1:
            if a > 0:
                count += bisect.bisect_right(nums2, x // a)
            elif a < 0:
                target = x // a
                if x % a != 0:
                    target += 1
                count += len(nums2) - bisect.bisect_left(nums2, target)
            else:
                if x >= 0:
                    count += len(nums2)
        
        return count        
    
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        low = -(10**10)
        high = 10**10

        while low < high:
            mid = (low + high) // 2
            if self.count_pairs(mid, nums1, nums2) < k:
                low = mid + 1
            else:
                high = mid

        return low
    
def main():
    sol = Solution()
    nums1 = [2,5]
    nums2 = [3,4]
    k = 2
    print(sol.kthSmallestProduct(nums1, nums2, k))
    
if __name__ == "__main__":
    main()