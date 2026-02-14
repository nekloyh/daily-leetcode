from typing import List
from bisect import bisect_right

maxF = lambda x, y: x if x > y else y  # noqa: E731

class Solution:    
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events = sorted(events, key=lambda x: (x[1]))
        n = len(events)
        ends = [event[1] for event in events]
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            start, _, val = events[i - 1]
            prev = bisect_right(ends, start - 1) - 1
            for j in range(1, k + 1):
                dp[i][j] = maxF(dp[i - 1][j], dp[prev + 1][j - 1] + val)
        
        return dp[-1][-1]
    
def main():
    sol = Solution()
    events = [[1, 2, 4], [3, 4, 3], [2, 3, 1]]   
    k = 2
    print(sol.maxValue(events, k))
    
if __name__ == "__main__":
    main()