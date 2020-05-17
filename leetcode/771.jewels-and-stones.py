#
# @lc app=leetcode id=771 lang=python3
#
# [771] Jewels and Stones
#

# @lc code=start
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        res = 0
        for j in set(J):
            res += S.count(j)
        return res
        """
        ✔ Accepted
        ✔ 254/254 cases passed (28 ms)
        ✔ Your runtime beats 75.88 % of python3 submissions
        ✔ Your memory usage beats 5.39 % of python3 submissions (13.9 MB)
        """

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(S.count(j) for j in set(J))
        """
        ✔ Accepted
        ✔ 254/254 cases passed (44 ms)
        ✔ Your runtime beats 18.17 % of python3 submissions
        ✔ Your memory usage beats 5.39 % of python3 submissions (13.8 MB)
        """

# @lc code=end
