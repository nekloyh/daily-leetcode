from collections import Counter

class Solution:
    def robotWithString(self, s: str) -> str:
        freq = Counter(s)
        t = []
        res = []
        min_char = 'a'
        
        for ch in s:
            t.append(ch)
            freq[ch] -= 1
            
            while freq[min_char] == 0 and min_char <= 'z':
                min_char = chr(ord(min_char) + 1)
                
            while t and t[-1] <= min_char:
                res.append(t.pop())
                
        return ''.join(res)
    
def main():
    sol = Solution()
    s = "zza"
    print(sol.robotWithString(s))
    
if __name__ == "__main__":
    main()
    