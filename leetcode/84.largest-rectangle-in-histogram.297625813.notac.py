#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#
# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
#
# algorithms
# Hard (33.27%)
# Likes:    2767
# Dislikes: 66
# Total Accepted:    219.9K
# Total Submissions: 660.9K
# Testcase Example:  '[2,1,5,6,2,3]'
#
# Given n non-negative integers representing the histogram's bar height where
# the width of each bar is 1, find the area of largest rectangle in the
# histogram.
#
# Above is a histogram where width of each bar is 1, given height =
# [2,1,5,6,2,3].
#
# The largest rectangle is shown in the shaded area, which has area = 10
# unit.
#
# Example:
#
# Input: [2,1,5,6,2,3]
# Output: 10

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea=[]
        for i in range(len(heights)):
            area=height=heights[i]
            for j in range(i, len(heights)):
                width=j-i+1
                height=min(height, heights[j])
                area=max(area, width*height)
            maxarea.append(area)
        return max(maxarea or [0])
# @lc code=end
