from typing import List
import heapq

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n, q = len(nums), len(queries)
        starts = [[] for _ in range(n)]
        for l, r in queries:
            starts[l].append(r)
        
        avail = []
        active = []
        chosen = 0
        
        for i in range(n):
            for r in starts[i]:
                heapq.heappush(avail, -r)
            
            while active and active[0] < i:
                heapq.heappop(active)
                
            need = nums[i] - len(active)
            
            for _ in range(need):
                while avail and -avail[0] < i:
                    heapq.heappop(avail)
                    
                if not avail:
                    return -1
                
                r = -heapq.heappop(avail)
                heapq.heappush(active, r)
                chosen += 1
                
        return q - chosen 

def main():
    nums = [1, 1, 1, 1]
    queries = [[1, 3], [0, 2], [1, 3], [1, 2]]
    
    sol = Solution()
    print(sol.maxRemoval(nums, queries))

if __name__ == '__main__':
    main()
    