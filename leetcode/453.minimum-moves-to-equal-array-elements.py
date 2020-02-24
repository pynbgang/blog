#
# @lc app=leetcode id=453 lang=python3
#
# [453] Minimum Moves to Equal Array Elements
#

# @lc code=start

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

# ping: brute force: time limit exceeded
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        res = 0
        while len(set(nums))>1:
            nums.sort()
            gaps = nums[-1] - nums[0]
            res += gaps
            nums = [nums[i]+gaps for i in range(len(nums)-1)] + [nums[-1]]
        return res

# does not meet "has to add for n-1 elements"
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        res = 0
        while len(set(nums))>1:
            print("len of nums set: %s is greater than 1" % set(nums))
            nums.sort()
            gaps = nums[-1] - nums[0]
            maxpos = nums.index(nums[-1])
            res += gaps
            #res += len(nums) - maxpos - 1
            nums = [nums[i]+gaps for i in range(maxpos)] + nums[maxpos:]
            print("after %d steps new nums looks: %s" % (gaps, nums))
        return res

# lmv
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - min(nums)*len(nums)

S=Solution()
nums=[1,2,3]
nums=[5,6,8,8,5]
S.minMoves(nums)

# @lc code=end
