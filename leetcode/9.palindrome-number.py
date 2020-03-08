#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        rev, div = 0, x
        while div:
            div, mod = divmod(div, 10)
            rev      = rev * 10 + mod
        return rev == x
# @lc code=end
