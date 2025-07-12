class Solution:
    def __init__(self):
        self.rMin = 6
        self.rMax = 1
        self.dp = [[[False] * 29 for _ in range(28)] for _ in range(6)]

    def f(self, round, l, r, n):  # noqa: E741
        if self.dp[round][l][r]:
            return
        self.dp[round][l][r] = True

        if l > r:
            return self.f(round, r, l, n)

        if l == r:
            self.rMin = min(self.rMin, round)
            self.rMax = max(self.rMax, round)
            return

        half = (n + 1) // 2
        iN = min(l, half)
        for i in range(1, iN + 1):
            j0 = max(l - i + 1, 1)
            for j in range(min(half, r) - i, j0 - 1, -1):
                if l + r - (i + j) <= n // 2:
                    self.f(round + 1, i, j, half)

    def earliestAndLatest(self, n, first, second):
        self.f(1, first, n + 1 - second, n)
        return [self.rMin, self.rMax]

def main():
    sol = Solution()
    n = 11
    firstPlayer = 2
    secondPlayer = 4
    print(sol.earliestAndLatest(n, firstPlayer, secondPlayer))
    
if __name__ == "__main__":
    main()