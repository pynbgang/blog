#
# @lc app=leetcode id=371 lang=python3
#
# [371] Sum of Two Integers
#

# @lc code=start
class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b:
            a, b = (a ^ b), (a & b) << 1
        return a

class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX_INT = 0x7FFFFFFF
        MIN_INT = 0x80000000
        MASK    = 0x100000000
        while b:
            a, b = (a ^ b) % MASK, ((a & b) << 1) % MASK
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)

class Solution:
    def getSum(self, a: int, b: int) -> int:
        if not b:
            return a
        return self.getSum(a^b, (a&b) << 1)

# @lc code=end
