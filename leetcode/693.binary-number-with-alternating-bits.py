#
# @lc app=leetcode id=693 lang=python3
#
# [693] Binary Number with Alternating Bits
#

# @lc code=start

class Solution(object):     #lmv: smart trick
    def hasAlternatingBits(self, n):
        return "00" not in bin(n) and "11" not in bin(n)
        """
        ✔ Accepted
        ✔ 204/204 cases passed (32 ms)
        ✔ Your runtime beats 39.62 % of python3 submissions
        ✔ Your memory usage beats 20 % of python3 submissions (13.9 MB)
        """

class Solution:     #ping: brute force, using all/any
    def hasAlternatingBits(self, n: int) -> bool:
        oddbits = [int(c) for c in bin(n)[2:][1::2]]
        evenbits = [int(c) for c in bin(n)[2:][::2]]
        return all(oddbits) and not any(evenbits) or not any(oddbits) and all(evenbits)
        """
        ✔ Accepted
        ✔ 204/204 cases passed (24 ms)
        ✔ Your runtime beats 91.72 % of python3 submissions
        ✔ Your memory usage beats 20 % of python3 submissions (13.8 MB)
        """

class Solution(object):  #owen: math
    def hasAlternatingBits(self, n):
        if n==0:return True
        if n%2!=0:
            temp=1
            while (temp<=n):
                if n==temp:return True
                temp=temp*4+1
            return False
        else:
            temp=2
            while(temp<=n):
                if n==temp:return True
                temp=temp*4+2
            return False

        """
        ✔ Accepted
        ✔ 204/204 cases passed (24 ms)
        ✔ Your runtime beats 91.72 % of python3 submissions
        ✔ Your memory usage beats 20 % of python3 submissions (13.6 MB)
        """

# @lc code=end
