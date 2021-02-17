#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:     #cheat
    def mySqrt(self, x: int) -> int:
        return int(sqrt(x))

class Solution:     #brute force
    def mySqrt(self, x: int) -> int:
        if not x: return 0
        if x in (1, 2): return 1
        for i in range(x):
            if i * i > x:
                return i-1

class Solution:     #ping: binary search: not done
    def mySqrt(self, x: int) -> int:
        if not x: return 0
        if x in (1, 2): return 1
        l, r = 0, x
        mid0 = mid = l + (r-l)//2
        toobig = toosmall = False
        while l <= r:
            mid = l + (r - l)//2
            if mid * mid > x:
                r = mid - 1
                toobig = True
            elif mid * mid < x:
                l = mid + 1
                toosmall = True
            else:
                return mid
            if toobig and toosmall: break
            mid0 = mid
        for mid in [mid0, mid]:
            if mid * mid <= x < (mid+1) * (mid+1):
                return mid

class Solution(object):     #lmv
    def mySqrt(self, x):
        l, r = 0, x
        while l <= r:
            mid = l + (r-l)//2
            if mid * mid <= x < (mid+1)*(mid+1):
                return mid
            elif mid * mid > x:
                r = mid - 1
            else:
                l = mid + 1

# @lc code=end
