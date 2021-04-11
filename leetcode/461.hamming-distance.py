#
# @lc app=leetcode id=461 lang=python3
#
# [461] Hamming Distance
#

# @lc code=start
class Solution:     #exactly same as lmv, finally...
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')

# @lc code=end
