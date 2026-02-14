from typing import List 

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        colors = [0, 1, 2]
        MOD = 10**9 + 7
        
        # create all posible pattern len m
        patterns = []
        def dfs(pos: int, current: List[int]):
            if pos == m:
                patterns.append(tuple(current))
                return
            
            for c in colors:
                if pos == 0 or current[pos - 1] != c:
                    dfs(pos + 1, current + [c])
        dfs(0, [])
        
        # valid i j: can pattern i and pattern j stand together
        P = len(patterns)
        valid = [[True] * P for _ in range(P)]
        
        for i in range(P):
            for j in range(i + 1, P):
                for pos in range(m):
                    if patterns[i][pos] == patterns[j][pos]:
                        valid[i][j] = False
                        break
        
        # setup for dp with dp[i][j] at cols i is pattern j
        dp = [[0] * P for _ in range(n)]
        for i in range(P):
            dp[0][i] = 1
            
        for i in range(1, n):
            for curr in range(P):
                for prev in range(curr + 1, P):
                    if valid[curr][prev]:
                        dp[i][curr] = (dp[i][curr] + dp[i - 1][prev]) % MOD
                        dp[i][prev] = (dp[i][prev] + dp[i - 1][curr]) % MOD
            
        return sum(dp[n - 1][i] for i in range(P)) % MOD
    
    
def main():
    m, n = 5, 5
    sol = Solution()
    print(sol.colorTheGrid(m, n))
    
if __name__ == "__main__":
    main()
    