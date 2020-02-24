#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
# ping: plain brute force: timeout
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(1, max(len(nums), max(nums or [0]))+1):
            if i not in nums:
                res.append(i)
        return res

# ping: passed
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        len1, nums = max(len(nums), max(nums or [0])), sorted(list(set(nums)))
        nums.insert(0, 0)
        nums.append(len1+1)
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] > 1:
                res.extend(range(nums[i]+1, nums[i+1]))
        return res

# lmv

    """
    https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/discuss/313703

    * Lang:    python3
    * Author:  ndave
    * Votes:   14
    """

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums:
            a = abs(n) - 1
            if nums[a] > 0: nums[a] *= -1
        return [i+1 for i in range(len(nums)) if nums[i] > 0]

# @lc code=end
