from typing import List

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: (p[0], -p[1]))
        n = len(points)
        res = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                _, yi = points[i]
                _, yj = points[j]
                
                if yj > yi:
                    continue

                blocked = False
                for k in range(i + 1, j):
                    _, yk = points[k]
                    if yj <= yk <= yi:
                        blocked = True
                        break

                if not blocked:
                    res += 1

        return res
    
def main():
    sol = Solution()
    points = [[1, 1], [2, 2], [3, 3]]
    print(sol.numberOfPairs(points))
    
if __name__ == "__main__":
    main()
    