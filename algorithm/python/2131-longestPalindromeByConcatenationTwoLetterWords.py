from typing import List
from collections import defaultdict

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        word_dictionary = defaultdict(int)
        for word in words:
            word_dictionary[word] += 1
        
        res = 0
        check = False
        for word in list(word_dictionary.keys()):
            if word[0] == word[1]:
                if word_dictionary[word] % 2:
                    check = True
                res += (word_dictionary[word] - (word_dictionary[word] % 2))
            else:
                palin = word[1] + word[0]
                res += min(word_dictionary[word], word_dictionary.get(palin, 0)) 
            
        return (res + check) * 2
    
def main():
    sol = Solution()
    print(sol.longestPalindrome(["lc", "cl", "gg"]))

if __name__ == "__main__":
    main()
    