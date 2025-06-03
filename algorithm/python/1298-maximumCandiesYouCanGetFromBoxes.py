from typing import List

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        q = initialBoxes
        mykeys = set()
        ans = 0
        prev = None
        while ans != prev:
            prev = ans
            nextq = []
            for curr in q:
                if curr in mykeys or status[curr]:
                    ans += candies[curr]
                    mykeys.update(keys[curr])
                    nextq.extend(containedBoxes[curr])
                else:
                    nextq.append(curr)
            q = nextq
        return ans
       
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