class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        lastBits = n & 1
        n >>= 1
        while n > 0 and lastBits != n & 1:
            lastBits = n & 1
            n >>= 1
        return n == 0
    
def main():
    s = Solution()
    print(s.hasAlternatingBits(5))

if __name__ == "__main__":
    main()
    