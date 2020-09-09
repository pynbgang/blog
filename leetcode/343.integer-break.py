#
# @lc app=leetcode id=343 lang=python3
#
# [343] Integer Break
#

# @lc code=start
class Solution:     #internet
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        result = 1
        while n > 4:
            n -= 3
            result *= 3
        return n * result
# @lc code=end
