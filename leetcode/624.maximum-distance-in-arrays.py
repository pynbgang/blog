#
# @lc app=leetcode id=624 lang=python3
#
# [624] Maximum Distance in Arrays
#

# @lc code=start
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        for array in arrays:
            l=[].extend(array)
        l.sort()
        l, j = 0, len(l)-1
        while True:
            low, high = l[i], l[j]
            for array in arrays:
                if not low in array and high in array:
                    return high-low
                else


# @lc code=end
