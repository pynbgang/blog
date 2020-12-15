#
# @lc app=leetcode id=1480 lang=python3
#
# [1480] Running Sum of 1d Array
#

# @lc code=start
class Solution:     #ping: initial
    def runningSum(self, nums: List[int]) -> List[int]:
        if not nums: return nums
        res = [nums[0]]
        for i in range(1, len(nums)):
            res.append(res[i-1]+nums[i])
        return res

class Solution:     #lmv
    #Time ```O(N)```
    #Space ```O(1)```
    def runningSum(self, nums):
        i = 1
        while i<len(nums):
            nums[i]+=nums[i-1]
            i+=1
        return nums

class Solution:     #ping: remove extra list
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1: return nums
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums

# @lc code=end
