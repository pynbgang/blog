#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:     #ping
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, l = 0, len(nums)
        while i < l:
            if nums[i]:
                i += 1
            else:
                nums.append(nums.pop(i))
                l -= 1

class Solution:     #lmv
    def moveZeroes(self, nums):
        zero = 0  # records the position of "0"
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1

# 1 2 3 4 0 0 5 6 0 7 8 9
# 1 2 3 4
# 1 2 3 4
#         z
#         5 z 0
#           6 z 0
#             7 z   0
#               8 z   0
#                 9 z   0

# @lc code=end
