from typing import List

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        tmp = 1
        for _ in range(n):
            res.append(tmp)
            
            if tmp * 10 <= n:
                tmp *= 10
            else:
                if tmp >= n:
                    tmp //= 10
                tmp += 1
                while tmp % 10 == 0:
                    tmp //= 10
        return res
    
def main():
    sol = Solution()
    n = 13
    print(sol.lexicalOrder(n))
    
if __name__ == "__main__":
    main()
    