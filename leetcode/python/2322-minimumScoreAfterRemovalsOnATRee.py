from typing import List


class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        xor = [0] * n
        parent = [0] * n
        in_time = [0] * n
        out_time = [0] * n
        time = 0
        stack = [(0, -1, False)]
        while stack:
            node, p, visited = stack.pop()
            if not visited:
                parent[node] = p
                in_time[node] = time
                time += 1
                stack.append((node, p, True))
                for neighbor in reversed(adj[node]):
                    if neighbor != p:
                        stack.append((neighbor, node, False))
            else:
                xor[node] = nums[node]
                for neighbor in adj[node]:
                    if neighbor != p:
                        xor[node] ^= xor[neighbor]
                out_time[node] = time - 1
        total_xor = xor[0]
        min_score = float("inf")
        for i in range(1, n):
            for j in range(i + 1, n):
                if in_time[i] < in_time[j] <= out_time[i]:
                    x = xor[j]
                    y = xor[i] ^ xor[j]
                    z = total_xor ^ xor[i]
                elif in_time[j] < in_time[i] <= out_time[j]:
                    x = xor[i]
                    y = xor[j] ^ xor[i]
                    z = total_xor ^ xor[j]
                else:
                    x = xor[i]
                    y = xor[j]
                    z = total_xor ^ x ^ y
                current_max = max(x, y, z)
                current_min = min(x, y, z)
                if current_max - current_min < min_score:
                    min_score = current_max - current_min
        return min_score #type: ignore
    
def main():
    sol = Solution()
    nums = [1, 5, 5, 4, 11]
    edges = [[0, 1], [1, 2], [1, 3], [3, 4]]
    print(sol.minimumScore(nums, edges))

if __name__ == "__main__":
    main()
    