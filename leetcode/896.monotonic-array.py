#
# @lc app=leetcode id=896 lang=python3
#
# [896] Monotonic Array
#

# @lc code=start
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        return A == sorted(A) or A == sorted(A, reverse=True)

# @lc code=end
