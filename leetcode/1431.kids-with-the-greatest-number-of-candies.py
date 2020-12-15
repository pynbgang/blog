#
# @lc app=leetcode id=1431 lang=python3
#
# [1431] Kids With the Greatest Number of Candies
#

# @lc code=start
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max1 = max(candies)
        return [True if max1 - extraCandies <= candies[i] else False for i in range(len(candies))]

# @lc code=end
