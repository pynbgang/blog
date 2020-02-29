#
# @lc app=leetcode id=1014 lang=python3
#
# [1014] Best Sightseeing Pair
#

# @lc code=start

class Solution:  # ping: brute force: timeout
    import sys
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        max1 = -sys.maxsize-1
        for i in range(len(A)-1):
            for j in range(i+1, len(A)):
                max1 = max(A[i]+A[j]+i-j, max1)
        return max1

class Solution:  #lmv
    """
    https://leetcode.com/problems/best-sightseeing-pair/discuss/400283

    * Lang:    python3
    * Author:  junaidmansuri
    * Votes:   0
    """

    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        maxi = max1 = 0
        for j in range(1, len(A)):
            maxi = max(maxi, A[i]+i)
            max1 = max(max1, maxi+A[j]-j)
        return max1

# @lc code=end
