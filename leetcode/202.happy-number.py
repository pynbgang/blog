#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:  # ping
    def isHappy(self, n: int) -> bool:
        set1 = set()
        while True:                 #keep running
            n = sum(int(i) ** 2 for i in str(n))  #update n w/ calculated result
            if n is 1:              #either get 1 and return True
                return True
            if n in set1:           #or get same num so conclude a loop
                return False
            set1.add(n)             #otherwise, update the set and keep running

        """
        ||   ✔ Accepted
        ||   ✔ 401/401 cases passed (24 ms)
        ||   ✔ Your runtime beats 96.99 % of python3 submissions
        ||   ✔ Your memory usage beats 100 % of python3 submissions (12.7 MB)
        """

class Solution:  # lmv (almost same as mine)
    """
    https://leetcode.com/problems/happy-number/discuss/56915

    * Lang:    python3
    * Author:  zyt6217315a
    * Votes:   110
    """

    def isHappy(self, n):
        mem = set()
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n in mem:
                return False
            else:
                mem.add(n)
        else:
            return True

# @lc code=end
