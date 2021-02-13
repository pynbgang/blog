#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution:     # brute force: timeout
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        else:
            for i in range(len(s)):
                s1 = s[:i] + s[i+1:]
                if s1 == s1[::-1]:
                    return True
        return False

class Solution:     #double pointer from LMV, ON, ON
    def validPalindrome(self, s: str) -> bool:
        p, q = 0, len(s)-1
        while p < q:
            if s[p] != s[q]:
                cut_l, cut_r = s[p+1:q+1], s[p:q]
                return cut_l == cut_l[::-1] or cut_r == cut_r[::-1]
            p += 1; q -= 1
        return True
# @lc code=end
