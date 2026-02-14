from typing import List

maxFunc = lambda x, y: x if x > y else y  # noqa: E731

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        res = 0
        sum_prefix = [0] * (n + 1)
        
        for i in range(n):
            sum_prefix[i + 1] = sum_prefix[i] + (endTime[i] - startTime[i])

        for i in range(k - 1, n):
            right = eventTime if i == n - 1 else startTime[i + 1]
            left = 0 if i == k - 1 else endTime[i - k]
            free_time = right - left - (sum_prefix[i + 1] - sum_prefix[i - k + 1])
            res = maxFunc(res, free_time)
        
        return res
    
def main():
    sol = Solution()
    eventTime = 10
    k = 1
    startTime = [0, 2, 9]
    endTime = [1, 4, 10]
    print(sol.maxFreeTime(eventTime, k, startTime, endTime))

if __name__ == "__main__":
    main()
    