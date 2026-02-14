import heapq
from typing import List

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        heap = []
        i = 0
        n = len(events)
        day = 0
        res = 0

        while i < n or heap:
            if not heap:
                day = events[i][0]

            while i < n and events[i][0] <= day:
                heapq.heappush(heap, events[i][1])
                i += 1

            while heap and heap[0] < day:
                heapq.heappop(heap)
                
            if heap:
                heapq.heappop(heap)
                res += 1
                
            day += 1
        
        return res
    
def main():
    sol = Solution()
    events = [[1, 5], [1, 5], [1, 5], [2, 3], [2, 3]]
    print(sol.maxEvents(events))

if __name__ == "__main__":
    main()