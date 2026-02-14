from typing import List
from math import ceil, log2

class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        max_ops = ceil(log2(k))
        shift_count = 0

        for op_index in range(max_ops - 1, -1, -1):
            half_length = 1 << op_index
            if k > half_length:
                k -= half_length
                shift_count += operations[op_index]

        return chr(ord("a") + shift_count % 26)

        
def main():
    sol = Solution()
    k = 5
    operations = [0, 0, 0]
    print(sol.kthCharacter(k, operations))

if __name__ == "__main__":
    main()