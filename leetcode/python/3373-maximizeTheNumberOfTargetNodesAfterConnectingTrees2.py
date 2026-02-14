from typing import List

class Solution:
    @staticmethod
    def build_graph(edges: List[List[int]]) -> List[List[int]]:
        adj = [[] for _ in range(len(edges) + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        return adj

    def dfsColor(self, adj, u, parent, color, isTreeA):
        if color[u] == 0:
            if isTreeA:
                self.evenA += 1
            else:
                self.evenB += 1
        else:
            if isTreeA:
                self.oddA += 1
            else:
                self.oddB += 1

        for v in adj[u]:
            if v != parent:
                color[v] = color[u] ^ 1
                self.dfsColor(adj, v, u, color, isTreeA)

    def maxTargetNodes(self, edges1, edges2):
        adjA = self.build_graph(edges1)
        adjB = self.build_graph(edges2)
        n, m = len(adjA), len(adjB)

        colorA = [-1] * n
        colorB = [-1] * m
        self.evenA = self.oddA = self.evenB = self.oddB = 0

        colorA[0] = 0  
        self.dfsColor(adjA, 0, -1, colorA, True)

        colorB[0] = 0
        self.dfsColor(adjB, 0, -1, colorB, False)

        res = [0] * n
        for i in range(n):
            if colorA[i] == 0:
                res[i] = self.evenA + max(self.oddB, self.evenB)
            else:
                res[i] = self.oddA + max(self.oddB, self.evenB)
        return res
    
        
def main():
    sol = Solution()
    edges1 = [[0, 1], [0, 2], [0, 3], [0, 4]]
    edges2 = [[0, 1], [1, 2], [2, 3]]
    print(sol.maxTargetNodes(edges1, edges2))

if __name__ == "__main__":
    main()
    