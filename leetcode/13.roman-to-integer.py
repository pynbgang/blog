#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
"""
    || Symbol       Value
    || I             1
    || V             5
    || X             10
    || L             50
    || C             100
    || D             500
    || M             1000
    || Input: "MCMXCIV"
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        sum, i, len1 = 0, 0, len(s)
        while i < len1:
            while i < len1 and s[i] is 'I':
                sum += 1
                i += 1
            while 0 < i < len1 and s[i] is 'V':
                sum += 4
                i += 1
            while i < len1 and s[i] is 'I':
                sum += 5
                i += 1
                while i < len1 and s[i] is 'I':
                    sum += 1
                    i += 1
                while i < len1 and s[i] is 'I':


# @lc code=end
