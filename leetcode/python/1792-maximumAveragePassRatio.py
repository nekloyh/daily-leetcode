from typing import List
import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def gain(passes, students):
            return (passes + 1) / (students + 1) - (passes / students)

        heap = [(-gain(passes, students), passes, students) for passes, students in classes]
        heapq.heapify(heap)

        for _ in range(extraStudents):
            _, passes, students = heapq.heappop(heap)
            passes, students = passes + 1, students + 1
            heapq.heappush(heap, (-gain(passes, students), passes, students))

        total = sum(passes / students for _, passes, students in heap)
        return total / len(classes)
    
def main():
    sol = Solution()
    classes = [[2, 4], [3, 9], [4, 5], [2, 10]]
    extraStudents = 4
    print(sol.maxAverageRatio(classes, extraStudents))
    
if __name__ == "__main__":
    main()
    