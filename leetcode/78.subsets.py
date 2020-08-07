#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return [[]]
        res = self.subsets(nums[1:])
        return res + [[nums[0]] + i for i in res]

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return [[]]
        res = self.subsets(nums[0:len(nums)-1])
        return res + [[nums[-1]] + i for i in res]

# @lc code=end
