class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        vowels = 0
        consonants = 0

        for c in word:
            if c.isalpha():
                if c.lower() in "aeiou":
                    vowels += 1
                else:
                    consonants += 1
            elif not c.isdigit():
                return False

        return vowels >= 1 and consonants >= 1

def main():
    sol = Solution()
    word = "234Adas"
    print(sol.isValid(word))

if __name__ == "__main__":
    main()
    