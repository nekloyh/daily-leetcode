from typing import List
from collections import deque

class Solution:
    @staticmethod
    def build_tree(edges: List[int]) -> List[List[int]]:
        adj = [[] for _ in range(len(edges))]
        for u, v in enumerate(edges):
            if v != -1:
                adj[u].append(v)
        return adj
    
    @staticmethod
    def bfs(adj: List[List[int]], node: int) -> List[int]:
        dist = [-1] * len(adj)
        q = deque()
        q.append(node)
        dist[node] = 0
        
        while q:
            u = q.popleft()
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)
            
        return dist 
    
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        adj = self.build_tree(edges)
        
        dist1 = self.bfs(adj, node1)
        dist2 = self.bfs(adj, node2)
        
        dist = float('inf')
        res = -1
        for i in range(len(edges)):
            if dist1[i] != -1 and dist2[i] != -1:
                curr_dist = max(dist1[i], dist2[i])
                if dist > curr_dist:
                    dist = curr_dist
                    res = i
        
        return res
    
def main():
    sol = Solution()
    edges = [2, 2, 3, -1]
    node1 = 0
    node2 = 1
    print(sol.closestMeetingNode(edges, node1, node2))  

if __name__ == "__main__":
    main()
    