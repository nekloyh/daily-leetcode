class Solution:
    @staticmethod
    def genString(word: str) -> str:
        n_word = ""
        for char in word:
            n_word += chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
        return n_word
    
    def kthCharacter(self, k: int) -> str:
        word = "a"
        while len(word) <= k:
            word += self.genString(word)
        return word[k - 1]
    
def main():
    sol = Solution()
    k = 5
    print(sol.kthCharacter(k))

if __name__ == "__main__":
    main()