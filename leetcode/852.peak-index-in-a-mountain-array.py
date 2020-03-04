#
# @lc app=leetcode id=852 lang=python3
#
# [852] Peak Index in a Mountain Array
#

# @lc code=start
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        return A.index(max(A))

        """
        ||   ✔ Accepted
        ||   ✔ 32/32 cases passed (64 ms)
        ||   ✔ Your runtime beats 99.84 % of python3 submissions
        ||   ✔ Your memory usage beats 96.97 % of python3 submissions (14 MB)
        """
# @lc code=end
