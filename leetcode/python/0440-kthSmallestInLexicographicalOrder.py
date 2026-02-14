class Solution:
    def _count_step(self, n: int, curr: int, next: int):
        steps = 0
        while curr <= n:
            steps += min(n + 1, next) - curr
            curr *= 10
            next *= 10
        return steps
            
    def findKthNumber(self, n: int, k: int) -> int:
        curr = 1
        k -= 1
        
        while k > 0:
            steps = self._count_step(n, curr, curr + 1)
            if steps <= k:
                curr += 1
                k -= steps
            else: 
                curr *= 10
                k -= 1
        
        return curr  
    
def main():
    sol = Solution()
    n = 13
    k = 2
    print(sol.findKthNumber(n, k))

if __name__ == "__main__":
    main()