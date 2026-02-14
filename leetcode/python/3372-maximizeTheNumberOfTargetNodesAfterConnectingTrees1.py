from typing import List
from collections import deque

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        def build_g(e):
            n = len(e) + 1
            g = [[] for _ in range(n)]
            for u, v in e:
                g[u].append(v)
                g[v].append(u)
            return g

        def bfs_cnt(g, d):
            n = len(g)
            res = [0] * n
            for s in range(n):
                vis = [0] * n
                q = deque()
                q.append((s, 0))
                vis[s] = 1
                cnt = 1
                while q:
                    u, dist = q.popleft()
                    if dist == d:
                        continue
                    for v in g[u]:
                        if not vis[v]:
                            vis[v] = 1
                            q.append((v, dist + 1))
                            cnt += 1
                res[s] = cnt
            return res

        g1 = build_g(edges1)
        g2 = build_g(edges2)

        if k == 0:
            return [1] * len(g1)

        cnt1 = bfs_cnt(g1, k)
        cnt2 = bfs_cnt(g2, k - 1)
        m2 = max(cnt2)

        return [x + m2 for x in cnt1]

    
    
def main():
    edges1 = [[0, 1], [0, 2], [2, 3], [2, 4]]
    edges2 = [[0, 1], [0, 2], [0, 3], [2, 7], [1, 4], [4, 5], [4, 6]]
    k = 1
    sol = Solution()
    ans = sol.maxTargetNodes(edges1, edges2, k)
    print(ans)


if __name__ == "__main__":
    main()
    