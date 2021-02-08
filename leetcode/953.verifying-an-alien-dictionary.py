#
# @lc app=leetcode id=953 lang=python3
#
# [953] Verifying an Alien Dictionary
#

# @lc code=start
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        return sorted(words, key=lambda x: "".join(chr(97+order.index(c)) for c in x)) == words
# @lc code=end
