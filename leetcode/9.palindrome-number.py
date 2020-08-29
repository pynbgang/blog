#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        rev, q = 0, x
        while q:
            q, r = q // 10, q % 10
            #q, r = divmod(q, 10)
            rev      = rev * 10 + r
        return rev == x

class Solution: #(Sat 29 Aug 2020 10:24:00 AM DST) cheating
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

# @lc code=end
