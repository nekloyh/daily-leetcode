from typing import List
from collections import Counter

class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.stable_list = sorted(nums1)
        self.counter_dist = Counter(nums2)
        self.unstable_list = nums2

    def add(self, index: int, val: int) -> None:
        old_val = self.unstable_list[index]
        self.counter_dist[old_val] -= 1
        
        if self.counter_dist[old_val] == 0:
            del self.counter_dist[old_val]
        
        self.unstable_list[index] += val
        new_val = self.unstable_list[index]
        self.counter_dist[new_val] += 1
        
    def count(self, tot: int) -> int:
        index = 0
        res = 0
        
        while index < len(self.stable_list):
            if self.stable_list[index] >= tot:
                break
            
            res += self.counter_dist.get(tot - self.stable_list[index], 0)
            
            index += 1
            
        return res
    
def main():
    operator = ["FindSumPairs", "count", "add", "count", "count", "add", "add", "count"]
    values = [[[1,1,2,2,2,3],[1,4,5,2,5,4]],[7],[3,2],[8],[4],[0,1],[1,1],[7]]
    
    obj = None
    output = []
    
    for op, val in zip(operator, values):
        if op == "FindSumPairs":
            obj = FindSumPairs(val[0], val[1])
            output.append("null")
        elif op == "add":
            if obj is not None:
                obj.add(val[0], val[1])
            output.append("null")
        elif op == "count":
            if obj is not None:
                result = obj.count(val[0])
            else:
                result = None
            output.append(result)
    
    print(output)

if __name__ == "__main__":
    main()
    