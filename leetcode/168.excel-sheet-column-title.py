#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start

class Solution:     #ping
    def convertToTitle(self, n: int) -> str:
        res = ""
        while n:
            res, n = chr(ord('A') + (n-1)%26) + res, (n-1)//26
        return res
        """
        ||   ✔ Accepted
        ||   ✔ 18/18 cases passed (32 ms)
        ||   ✔ Your runtime beats 52.05 % of python3 submissions
        ||   ✔ Your memory usage beats 11.03 % of python3 submissions (14.4 MB)
        """

class Solution:     #lmv
    # @return a string
    def convertToTitle(self, num):
        capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        result = []
        while num > 0:
            result.append(capitals[(num-1)%26])
            num = (num-1) // 26
        result.reverse()
        return ''.join(result)

# @lc code=end
