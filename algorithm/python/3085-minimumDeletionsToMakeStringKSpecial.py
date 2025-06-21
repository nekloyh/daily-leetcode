from collections import Counter

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:

        freq = list(Counter(word).values())
        res = float("inf")

        for target in freq:
            deletions = 0
            for f in freq:
                if f < target:
                    deletions += f
                elif f - target > k:
                    deletions += f - (target + k)
            res = min(res, deletions)

        return int(res)


def main():
    sol = Solution()
    word = "aabcaba"
    k = 0
    print(sol.minimumDeletions(word, k))

if __name__ == "__main__":
    main()