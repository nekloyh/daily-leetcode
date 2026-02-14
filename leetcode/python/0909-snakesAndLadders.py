from typing import List
from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        min_rolls = [-1] * (n * n + 1)
        q = deque()
        q.append(1)
        min_rolls[1] = 0
        
        while q:
            u = q.popleft()
            for i in range(1, 7):
                v = u + i
                if v > n * n:
                    break
                row = (v - 1) // n
                col = (v - 1) % n
                pos = board[n - 1 - row][(n - 1 - col) if (row % 2 == 1) else col]
                y = pos if pos > 0 else v
                if y == n * n:
                    return min_rolls[u] + 1
                if min_rolls[y] == -1:
                    min_rolls[y] = min_rolls[u] + 1
                    q.append(y)

        return -1
    
def main():
    board = [
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 35, -1, -1, 13, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 15, -1, -1, -1, -1],
    ]
    sol = Solution()
    print(sol.snakesAndLadders(board))

if __name__ == "__main__":
    main()
    