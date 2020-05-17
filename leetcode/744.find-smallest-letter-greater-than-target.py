#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#

# @lc code=start
class Solution:  #ping
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters.append(target); letters.sort(reverse=True) #merge and reversely sort
        return letters[(letters.index(target) - 1)] #find the one ahead of target
        """
        ✔ Accepted
        ✔ 165/165 cases passed (184 ms)
        ✔ Your runtime beats 5.83 % of python3 submissions
        ✔ Your memory usage beats 14.29 % of python3 submissions (14 MB)
        """

# @lc code=end
