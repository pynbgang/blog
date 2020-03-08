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

class Solution:     #ping: gave up
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

class Solution:     #lmv: convert all substraction to addition
    def romanToInt(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number

class Solution:     #wangmazi, compare adjacent nums to decide - or +
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        ROMAN = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        if s == "":
            return 0
        index = len(s) - 2
        sum = ROMAN[s[-1]]
        while index >= 0:
            if ROMAN[s[index]] < ROMAN[s[index + 1]]:
                sum -= ROMAN[s[index]]
            else:
                sum += ROMAN[s[index]]
            index -= 1
        return sum

# @lc code=end
