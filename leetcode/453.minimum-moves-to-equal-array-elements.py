#
# @lc app=leetcode id=453 lang=python3
#
# [453] Minimum Moves to Equal Array Elements
#

# @lc code=start

# lmv
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - min(nums)*len(nums)

# ping: brute force: recursive: failed
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        self.res = 0
        self.helper(nums)
        return self.res

    def helper(self, nums):
        print("get nums: ", nums)
        while len(set(nums))>1:
            print("len of nums set: %s is greater than 1" % set(nums))
            nums.sort()
            gaps = nums[-1] - nums[0]
            self.res += gaps
            nums = [nums[i]+gaps for i in range(len(nums)-1)] + [nums[-1]]
            print("after %d steps new nums looks: %s" % (gaps, nums))
            self.helper(nums)
        else:
            print("len of nums set: %s is less than 1" % set(nums))

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        res = 0
        while len(set(nums))>1:
            nums.sort()
            gaps = nums[-1] - nums[0]
            res += gaps
            nums = [nums[i]+gaps for i in range(len(nums)-1)] + [nums[-1]]
        return res

S=Solution()
nums=[1,2,3]
S.minMoves(nums)

# @lc code=end
