from typing import List


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = list()
        for i, word in enumerate(words):
            if x in word:
                res.append(i)
        return res


def main():
    words = ["leet","code"]
    x = "e"
    sol = Solution()
    print(sol.findWordsContaining(words, x))


if __name__ == "__main__":
    main()
