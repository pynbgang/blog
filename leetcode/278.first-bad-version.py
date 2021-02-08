#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:     #lmv
    def firstBadVersion(self, n):
        l, r = 0, n-1
        while(l<=r):
            mid = l + (r-l)//2
            if isBadVersion(mid):
                r = mid-1
            else:
                l = mid+1
        return l
# @lc code=end
