import bisect
from typing import List


class Solution:
    def maxTaskAssign(
        self, tasks: List[int], workers: List[int], pills: int, strength: int
    ) -> int:
        n, m = len(tasks), len(workers)
        tasks.sort()
        workers.sort()
        ll, rr = 0, min(n, m)

        while ll < rr:
            mid = (ll + rr + 1) // 2
            usedPills = 0
            avail = workers[-mid:].copy()
            canAssign = True

            for t in reversed(tasks[:mid]):
                if avail[-1] >= t:
                    avail.pop()
                else:
                    idx = bisect.bisect_left(avail, t - strength)
                    if idx == len(avail) or usedPills == pills:
                        canAssign = False
                        break
                    usedPills += 1
                    avail.pop(idx)

            if canAssign:
                ll = mid
            else:
                rr = mid - 1

        return ll
    
def main():
    sol = Solution()
    tasks = [3, 2, 1]
    workers = [0, 3, 3]
    pills = 1
    strength = 1
    print(sol.maxTaskAssign(tasks, workers, pills, strength)) 


if __name__ == "__main__":
    main()
    