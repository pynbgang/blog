#
# @lc app=leetcode id=135 lang=python3
#
# [135] Candy
#

# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        res, higher = len(ratings), 0
        if ratings[0] > ratings[1]:
            res += 1
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                res += 1
                higher += 1
                res += higher - 1
            else:
                higher = 0
                if i >=2 and ratings[i] < ratings[i-1] and ratings[i-1] >= ratings[i-2]:
                    res += 1
        return res

class Solution:     #lmv
    """
    Python two pass solution (left to right, then right to left).

    https://leetcode.com/problems/candy/discuss/42881

    * Lang:    python3
    * Author:  OldCodingFarmer
    * Votes:   16
    """
    def candy(self, ratings):
        res = len(ratings) * [1]
        for i in range(1, len(ratings)):  # from left to right
            if ratings[i] > ratings[i-1]:
                res[i] = res[i-1] + 1
        for i in range(len(ratings)-1, 0, -1):  # from right to left
            if ratings[i-1] > ratings[i]:
                res[i-1] = max(res[i-1], res[i]+1)
        return sum(res)

class Solution:     #playing lmv
    def candy(self, ratings):
        res = len(ratings) * [1]
        for i in range(1, len(ratings)):  # from left to right
            if ratings[i] > ratings[i-1]:
                res[i] = max(res[i-1]+1, res[i])
        for i in range(len(ratings)-1, 0, -1):  # from right to left
            if ratings[i-1] > ratings[i]:
                res[i-1] = max(res[i-1], res[i]+1)
        return sum(res)



# @lc code=end
