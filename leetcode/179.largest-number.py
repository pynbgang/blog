#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#
# https://leetcode.com/problems/largest-number/description/
#
# algorithms
# Medium (32.24%)
# Likes:    4205
# Dislikes: 376
# Total Accepted:    290.5K
# Total Submissions: 901.1K
# Testcase Example:  '[10,2]'
#
# Given a list of non-negative integers nums, arrange them such that they form
# the largest number and return it.
#
# Since the result may be very large, so you need to return a string instead of
# an integer.
#
#
# Example 1:
#
#
# Input: nums = [10,2]
# Output: "210"
#
#
# Example 2:
#
#
# Input: nums = [3,30,34,5,9]
# Output: "9534330"
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 10^9
#
#
#

# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
# @lc code=end
