#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#

# @lc code=start
class Solution:  #ping: wrong, can't sort
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        return sum(sorted(nums)[-1:-k-1:-1])/k

class Solution:  #ping: time limit exceeded
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        return max(sum(nums[i:i+k]) for i in range(len(nums)-k+1))/k

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        M = d = 0
        for i in range(len(nums)-k):
            d += nums[i+k] - nums[i]
            if d > M: M = d
        return (sum(nums[:k])+M)/k

# @lc code=end
