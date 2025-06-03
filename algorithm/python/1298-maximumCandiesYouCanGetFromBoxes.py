from typing import List
from collections import deque

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(status)
        is_opened = [0] * n
        has_box = [0] * n
        
        q = deque()
        for box in initialBoxes:
            has_box[box] = 1
            q.append(box)

        res = 0
        changed = True
        
        while changed:
            changed = False
            for _ in range(len(q)):
                cur_box = q.popleft()
                
                if is_opened[cur_box] or status[cur_box] == 0:
                    q.append(cur_box)
                    continue

                is_opened[cur_box] = 1
                res += candies[cur_box]
                changed = True

                for box in containedBoxes[cur_box]:
                    if not has_box[box]:
                        q.append(box)
                        has_box[box] = 1
                    else:
                        q.append(box)

                for key in keys[cur_box]:
                    if status[key] == 0:
                        status[key] = 1
                        if has_box[key]:
                            q.append(key)
        return res
       
def main():
    sol = Solution()
    status = [1,0,1,0]
    candies = [7,5,4,100]
    keys = [[],[],[1],[]]
    containedBoxes = [[1,2],[3],[],[]]
    initialBoxes = [0]
    print(sol.maxCandies(status, candies, keys, containedBoxes, initialBoxes))  

if __name__ == "__main__":
    main()