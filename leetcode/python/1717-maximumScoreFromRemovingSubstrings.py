class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x < y:
            x, y = y, x
            a, b = 'b', 'a'
        else:
            a, b = 'a', 'b'

        score = count_a = count_b = 0
        for ch in s:
            if ch == a:
                count_a += 1
            elif ch == b:
                if count_a > 0:
                    count_a -= 1
                    score += x
                else:
                    count_b += 1
            else:
                score += min(count_a, count_b) * y
                count_a = count_b = 0

        score += min(count_a, count_b) * y
        return score

def main():
    sol = Solution()
    s = "cdbcbbaaabab"
    x = 4
    y = 5
    print(sol.maximumGain(s, x, y))
    
if __name__ == "__main__":
    main()
    