#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(i*i for i in A)
        """
        ||   ✔ Accepted
        ||   ✔ 132/132 cases passed (200 ms)
        ||   ✔ Your runtime beats 100 % of python3 submissions
        ||   ✔ Your memory usage beats 94.05 % of python3 submissions (14.7 MB)
        """
# @lc code=end
