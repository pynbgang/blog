#
# @lc app=leetcode id=263 lang=python3
#
# [263] Ugly Number
#

# @lc code=start
class Solution:     #ping: prime issue
    def isUgly(self, num: int) -> bool:
        num1, i, set1 = num, 2, set()
        while i**2 <= num:
            if not num % i:
                set1.add(i)
                num //= i
            else:
                i += 1
        set1.add(num)   #don't forget the last factor
        return True if set1.issubset({2,3,5}) or num1==1 else False

        """
        ||   ✔ Accepted
        ||   ✔ 1012/1012 cases passed (604 ms)
        ||   ✔ Your runtime beats 5.44 % of python3 submissions
        ||   ✔ Your memory usage beats 100 % of python3 submissions (12.7 MB)
        """

class Solution:     #lmv
    def isUgly(self, num: int) -> bool:
        for p in 2, 3, 5:
            #while num % p == 0 < num:      #zb way
            while not num % p and num>0:    #normal way
                num //= p
        return num == 1

        """
        ||   ✔ Accepted
        ||   ✔ 1012/1012 cases passed (28 ms)
        ||   ✔ Your runtime beats 76.09 % of python3 submissions
        ||   ✔ Your memory usage beats 100 % of python3 submissions (12.8 MB)
        """

# @lc code=end
