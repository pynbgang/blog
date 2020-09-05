#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        pass

class Solution: #jj
    def trap(self, height: List[int]) -> int:
        res, lbar, rbar, l, r = 0, 0, 0, 0, len(height) - 1
        while l < r:
            lbar, rbar = max(lbar, height[l]), max(rbar, height[r])
            if lbar < rbar:
                res, l = res + lbar - height[l], l + 1
            else:
                res, r = res + rbar - height[r], r - 1
        return res

class Solution: #ping, per http://logos23333.top/algorithm/2017/12/04/leetcode-42/
    def trap(self, height: List[int]) -> int:
        return sum(min(max(height[:i+1]), max(height[i:])) - height[i] for i in range(len(height)))

"""
%%timeit -r 3 -n 10
S=Solution()
height = [2,1,3,5,2,3,4]*100
S.trap(height)
"""

# @lc code=end
