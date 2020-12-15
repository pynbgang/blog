#
# @lc app=leetcode id=1119 lang=python3
#
# [1119] Remove Vowels from a String
#

# @lc code=start
class Solution:
    def removeVowels(self, s: str) -> str:
        res = ""
        for c in s:
            if c not in "aeiou":
                res += c
        return res
    def removeVowels(self, s: str) -> str:
        return "".join(c for c in s if c not in "aeiou")
# @lc code=end
