class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        cnt_N = cnt_E = cnt_S = cnt_W = 0
        res = 0

        for ch in s:
            if ch == "N":
                cnt_N += 1
            elif ch == "W":
                cnt_W += 1
            elif ch == "S":
                cnt_S += 1
            else:
                cnt_E += 1

            len_x = min(cnt_E, cnt_W, k)
            len_y = min(cnt_N, cnt_S, k - len_x)
            

            res = max(
                res, 
                abs(cnt_E - cnt_W) + len_x * 2 + abs(cnt_N - cnt_S) + len_y * 2
            )

        return res
    
def main():
    sol = Solution()
    s = "NWSE"
    k = 1
    print(sol.maxDistance(s, k))
    
if __name__ == "__main__":
    main()