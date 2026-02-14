from typing import List

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = [s[i: i + k] for i in range(0, len(s), k)]
        if len(res[-1]) < k:
            res[-1] += fill * (k - len(res[-1])) 
        return res
    
def main():
    s = "abcdefghij"
    k = 3
    fill = 'x'
    sol = Solution()
    print(sol.divideString(s, k, fill))

if __name__ == "__main__":
    main()