class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s
        
        res = s[:2]
        pos = 2
        while pos < len(s):
            if s[pos] == s[pos - 1] and s[pos] == s[pos - 2]:
                pos += 1
                continue
            else:
                res += s[pos]
                pos += 1
            
        return res
    
def main():
    sol = Solution()
    s = "leeetcode"
    print(sol.makeFancyString(s))
    
if __name__ == "__main__":
    main()
    