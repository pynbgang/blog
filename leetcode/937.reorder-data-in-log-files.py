#
# @lc app=leetcode id=937 lang=python3
#
# [937] Reorder Data in Log Files
#

# @lc code=start
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def helper(s):
            l = s.split()
            let = True if str(l[1]) > str('0') else False

        return sorted(logs, key=helper)
# @lc code=end
