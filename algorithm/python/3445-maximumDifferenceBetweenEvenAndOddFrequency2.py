class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        res = float('-inf')
        
        for a in range(5):
            for b in range(5):
                if a == b:
                    continue
                
                s1 = [0] * (n + 1)
                s2 = [0] * (n + 1)
                
                for i in range(1, n + 1):
                    s1[i] = s1[i - 1] + (int(s[i - 1]) == a)
                    s2[i] = s2[i - 1] + (int(s[i - 1]) == b)

                g = [[float("-inf")] * 2 for _ in range(2)]
                j = 0

                for i in range(k, n + 1):
                    while i - j >= k and s1[i] > s1[j] and s2[i] > s2[j]:
                        pa = s1[j] % 2
                        pb = s2[j] % 2
                        g[pa][pb] = max(g[pa][pb], s2[j] - s1[j])
                        j += 1

                    pa = s1[i] % 2
                    pb = s2[i] % 2
                    best = g[1 - pa][pb]
                    if best != float("-inf"):
                        res = max(res, s1[i] - s2[i] + best)
                        
        return -1 if res == float("-inf") else int(res)
    

def main():
    s = "12233"
    k = 4
    sol = Solution()
    print(sol.maxDifference(s, k))
    

if __name__ == "__main__":
    main()