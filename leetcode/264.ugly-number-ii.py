#
# @lc app=leetcode id=264 lang=python3
#
# [264] Ugly Number II
#

# @lc code=start

class Solution:  #ping: use #263 and brute force, time exceeded
    def nthUglyNumber(self, n: int) -> int:
        i, num, num1 = 0, 1, 1
        while i < n:
            num = num1
            for p in 2,3,5:
                while num % p == 0 < num:
                    num //= p
            if num == 1:
                i += 1
            num1 += 1
        return num1-1

class Solution:  #lmv
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        while n > 1:
            u2, u3, u5 = 2 * ugly[i2], 3 * ugly[i3], 5 * ugly[i5]
            umin = min((u2, u3, u5))
            if umin == u2:
                i2 += 1
            if umin == u3:
                i3 += 1
            if umin == u5:
                i5 += 1
            ugly.append(umin)
            n -= 1
        return ugly[-1]

# @lc code=end
