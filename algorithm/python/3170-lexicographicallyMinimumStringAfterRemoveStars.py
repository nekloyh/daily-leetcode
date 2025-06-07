class Solution:
    def clearStars(self, s: str) -> str:
        freq = [[-1] for _ in range(26)]
        n = len(s)
        
        for i in range(n):
            if s[i] != '*':
                freq[ord(s[i]) - ord('a')].append(i)
            else:
                for j in range(26):
                    if freq[j][-1] != -1:
                        freq[j].pop()
                        break
        
        pool = []
        for i in range(26):
            while freq[i][-1] != -1:
                pool.append((i, freq[i][-1]))
                freq[i].pop()
                
        pool_sorted = sorted(pool, key=lambda x: x[1])
        res = ""
        for pair in pool_sorted:
            res = res + chr(pair[0] + ord("a"))
        return res
    
def main():
    sol = Solution()
    s = "aaba*"
    print(sol.clearStars(s))

if __name__ == "__main__":
    main()
    