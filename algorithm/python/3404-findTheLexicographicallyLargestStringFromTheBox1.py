class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        n = len(word)
        res = ""
        length = n - numFriends + 1
        for i in range(0, n):
            sub = word[i : i + length]
            if sub > res:
                res = sub
        return res
    
def main():
    sol = Solution()
    word = "bf"
    numFriends = 2
    print(sol.answerString(word, numFriends))

if __name__ == "__main__":
    main()
    