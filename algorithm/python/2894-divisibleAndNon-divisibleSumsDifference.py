class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        res = sum([i * (1 if i % m else -1) for i in range(n + 1)])
        return res
    
def main():
    sol = Solution()
    n, m = 10, 3
    print(sol.differenceOfSums(n, m))

if __name__ == "__main__":
    main()