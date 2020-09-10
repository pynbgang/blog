#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#

# @lc code=start
class Solution:             #owen
    def singleNumber(self, nums: List[int]) -> int:
        return (sum(set(nums))*3 - sum(nums))//2

class Solution(object):     #lmv
    def singleNumber(self, nums):
        one, two = 0, 0
        for x in nums:
            one, two, three = one ^ x, two | (one & x), two & x
            one, two = one & ~three, two & ~three
        return one

class Solution:             #ping
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) <= 3: return nums[-1]
        nums.sort()
        if nums[0] != nums[1]: return nums[0]
        if nums[-1] != nums[-2]: return nums[-1]
        for i in range(1, len(nums)-1):
            if nums[i] != nums[i-1] and nums[i+1] != nums[i]:
                return nums[i]


# @lc code=end
