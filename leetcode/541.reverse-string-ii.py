#
# @lc app=leetcode id=541 lang=python3
#
# [541] Reverse String II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        #res=""
        #for i in range(0, len(s), 2*k):
        #    res += s[i:i+k][::-1] + s[i+k:i+2*k]
        #return res
        return "".join(s[i:i+k][::-1] + s[i+k:i+2*k] for i in range(0, len(s), 2*k))

#a b c d e f g
#0 1|2 3|4 5 6
#    k   2k
#i       i
#
# @lc code=end
