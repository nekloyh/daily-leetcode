class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        cnt, val = 0, 0
        bits = k.bit_length()
        
        for i, ch in enumerate(s[::-1]):
            if ch == "1":
                if i < bits and val + (1 << i) <= k:
                    val += 1 << i
                    cnt += 1
            else:
                cnt += 1
        
        return cnt
        
    
def main():
    sol = Solution()
    s = "1001010"
    k = 5
    print(sol.longestSubsequence(s, k))

if __name__ == "__main__":
    main()