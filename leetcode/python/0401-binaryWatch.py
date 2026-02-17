from typing import List

class Solution:
    def countBits(self, n: int) -> int:
        cnt = 0
        while n:
            cnt += n & 1
            n >>= 1
        return cnt
    
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        for h in range(12):
            for m in range(60):
                if self.countBits(h) + self.countBits(m) == turnedOn:
                    res.append(f"{h}:{m:02d}")
        return res
    
def main():
    s = Solution()
    print(s.readBinaryWatch(1))

if __name__ == "__main__":
    main()
    