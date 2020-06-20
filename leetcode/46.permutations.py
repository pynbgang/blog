#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution(object):
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums: return
        self.l, len1 = [], len(nums)
        self.helper(nums, [], len1)
        return self.l

    def helper(self, nums, list1, len1):
        if len(list1) == len1:
            self.l.append(list1)
            return
        for i in range(len(nums)):
            self.helper(nums[0:i] + nums[i+1:], list1 + [nums[i]], len1)
# @lc code=end
