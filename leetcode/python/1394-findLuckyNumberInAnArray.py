from typing import List
from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        res = -1
        arr_counter = Counter(arr)
        for value, key in arr_counter.items():
            if value == key:
                res = max(res, value)
        return res
        
def main():
    sol = Solution()
    arr = [2,2,3,4]
    print(sol.findLucky(arr))
    
if __name__ == "__main__":
    main()