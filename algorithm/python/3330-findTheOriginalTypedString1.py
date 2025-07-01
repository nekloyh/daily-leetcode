class Solution:
    def possibleStringCount(self, word: str) -> int:
        n = len(word)
        cnt = n
        for i in range(1, n):
            if word[i] != word[i - 1]:
                cnt -= 1
        return cnt
    
def main():
    word = "abbcccc"
    sol = Solution()
    print(sol.possibleStringCount(word))

if __name__ == "__main__":
    main()