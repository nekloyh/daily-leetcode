from collections import deque


class Solution:
    @staticmethod
    def isK(sub: str, t: str, k: int) -> bool:
        count = i = 0
        for ch in t:
            if i < len(sub) and ch == sub[i]:
                i += 1
                if i == len(sub):
                    i = 0
                    count += 1
                    if count == k:
                        return True
        return False
    
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        res = ""
        q = deque([""])
        while q:
            curr = q.popleft()
            for ch in map(chr, range(ord('a'), ord('z') + 1)):
                nxt = curr + ch
                if self.isK(nxt, s, k):
                    res = nxt
                    q.append(nxt)
        return res
    
def main():
    s = "letsleetcode"
    k = 2
    sol = Solution()
    print(sol.longestSubsequenceRepeatedK(s, k))

if __name__ == "__main__":
    main()
    