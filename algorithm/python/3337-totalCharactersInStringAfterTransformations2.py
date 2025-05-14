from typing import List

class Matrix:
    def __init__(self, size=26, mod=10**9 + 7):
        self.n = size
        self.MOD = mod

    def identity(self):
        return [[int(i == j) for j in range(self.n)] for i in range(self.n)]

    def mul(self, A, B):
        res = [[0] * self.n for _ in range(self.n)]
        for i in range(self.n):
            for k in range(self.n):
                if A[i][k]:
                    for j in range(self.n):
                        res[i][j] = (res[i][j] + A[i][k] * B[k][j]) % self.MOD
        return res

    def exp(self, A, power):
        res = self.identity()
        while power:
            if power % 2:
                res = self.mul(res, A)
            A = self.mul(A, A)
            power //= 2
        return res


class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        matrix = Matrix()
        base = [[0] * 26 for _ in range(26)]

        for ch in range(26):
            for r in range(1, nums[ch] + 1):
                base[(ch + r) % 26][ch] += 1

        base_t = matrix.exp(base, t)
        res = 0
        for ch in s:
            col = ord(ch) - ord("a")
            res = (res + sum(base_t[row][col] for row in range(26))) % matrix.MOD

        return res


def main():
    s = "abcyy"
    t = 2
    nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]
    
    sol = Solution()
    print(sol.lengthAfterTransformations(s, t, nums))
    
if __name__ == "__main__":
    main()
    