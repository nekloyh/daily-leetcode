class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        MOD = 10 ** 9 + 7
        encode_word = [1]
        for pos in range(1, len(word)):
            if word[pos] == word[pos - 1]:
                encode_word[-1] += 1
            else:
                encode_word.append(1)
        
        total = 1
        for num in encode_word:
            total = (total * num) % MOD
        
        if k <= len(encode_word):
            return total
        
        dp = [0] * k
        dp[0] = 1
        
        for num in encode_word:
            n_dp = [0] * k
            sum_val = 0
            for s in range(k):
                if s > 0:
                    sum_val = (sum_val + dp[s - 1]) % MOD
                if s > num:
                    sum_val = (sum_val - dp[s - num - 1] + MOD) % MOD
                n_dp[s] = sum_val
            dp = n_dp    
        
        invalid = sum(dp[len(encode_word) : k]) % MOD
        return (total - invalid + MOD) % MOD
    
def main():
    sol = Solution()
    word = "aabbccdd"
    k = 7
    print(sol.possibleStringCount(word, k))

if __name__ == "__main__":
    main()