from typing import List
import math

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: (p[0], -p[1]))
        n = len(points)
        res = 0
        
        for i in range(n):
            yi = points[i][1]
            max_y = -math.inf
            
            for j in range(i + 1, n):
                yj = points[j][1]
                
                if yj <= yi:
                    if yj > max_y:
                        res += 1
                        max_y = yj
        
        return res
    
def main():
    sol = Solution()
    points = [[1, 1], [2, 2], [3, 3]]
    print(sol.numberOfPairs(points))
    
if __name__ == "__main__":
    main()
    