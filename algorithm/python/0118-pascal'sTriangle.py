from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        if numRows == 1:
            return res
        
        for i in range(2, numRows + 1):
            tmp = [1]
            for j in range(1, i - 1):
                tmp.append(res[-1][j - 1] + res[-1][j])
            tmp.append(1)
            res.append(tmp)
            
        return res
    
def main():
    sol = Solution()
    numRows = 5
    print(sol.generate(numRows))
    
if __name__ == "__main__":
    main()
    