from typing import List
import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        available = list(range(n))
        busy = []
        heapq.heapify(available)
        useCount = [0] * n
        meetings.sort()

        for start, end in meetings:
            while busy and busy[0][0] <= start:
                _, room = heapq.heappop(busy)
                heapq.heappush(available, room)

            duration = end - start

            if available:
                room = heapq.heappop(available)
                heapq.heappush(busy, (end, room))
                useCount[room] += 1
            else:
                earliest_end, room = heapq.heappop(busy)
                heapq.heappush(busy, (earliest_end + duration, room))
                useCount[room] += 1

        return max(range(n), key=lambda x: (useCount[x], -x))
    
def main():
    sol = Solution()
    n = 3
    m = [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]
    print(sol.mostBooked(n, m))

if __name__ == "__main__":
    main()
